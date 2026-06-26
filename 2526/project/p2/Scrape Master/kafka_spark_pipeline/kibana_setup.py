"""
================================================================================
 Kibana data-view + visualisations + dashboard setup
 SECP3133 Project 2 · Member 3 (Pipeline & Visualization)
================================================================================

Idempotently creates the Kibana objects backing the FUZZ CHANNEL dashboard:

  1. Data view  : `youtube_sentiment` (pattern `youtube_sentiment*`, time field
                  `published_at`)
  2. Lens viz   : Sentiment label distribution (donut)
  3. Lens viz   : Sentiment over time (stacked bars by published_at)
  4. Lens viz   : Top 10 videos by sentiment (horizontal bar)
  5. Tag-cloud  : Comment word cloud (significant terms on comment_text)
  6. Dashboard  : "FUZZ CHANNEL Sentiment" — embeds 1-5 in a 2x2 grid

We talk to Kibana over HTTP rather than shipping an NDJSON because the saved-
object migration format is fragile across Kibana 8.x patch releases. This
script just calls the documented `/api/saved_objects/...` endpoints and is
trivially re-runnable.

────────────────────────────────────────────────────────────────────────────────
 Usage
────────────────────────────────────────────────────────────────────────────────
  python kafka_spark_pipeline/kibana_setup.py                # create everything
  python kafka_spark_pipeline/kibana_setup.py --delete       # nuke + recreate from scratch

  Override the host with KIBANA_HOST=http://host:port (default localhost:5601).
================================================================================
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import requests

KIBANA_HOST   = os.environ.get("KIBANA_HOST", "http://localhost:5601")
DATA_VIEW_ID  = "youtube-sentiment-dataview"
INDEX_PATTERN = "youtube_sentiment*"
TIME_FIELD    = "published_at"
HEADERS       = {"kbn-xsrf": "true", "Content-Type": "application/json"}

# Fixed colour mapping for the three sentiment classes. Saved into each
# visualisation's uiStateJSON so Kibana doesn't fall back to its default
# palette and assign random hues per refresh.
SENTIMENT_COLOURS = {
    "negative": "#E53935",   # vibrant red
    "neutral":  "#1E88E5",   # vibrant blue
    "positive": "#43A047",   # vibrant green
}
_UI_STATE_COLOURS = json.dumps({"vis": {"colors": SENTIMENT_COLOURS}})


# ── Data view ──────────────────────────────────────────────────────────────
def create_data_view(base: str) -> dict:
    payload = {
        "data_view": {
            "id":         DATA_VIEW_ID,
            "name":       "youtube_sentiment",
            "title":      INDEX_PATTERN,
            "timeFieldName": TIME_FIELD,
        }
    }
    r = requests.post(f"{base}/api/data_views/data_view",
                      headers=HEADERS, data=json.dumps(payload))
    if r.status_code in (200, 201):
        print(f"[kibana] created data view '{DATA_VIEW_ID}'")
    elif r.status_code == 409:
        print(f"[kibana] data view '{DATA_VIEW_ID}' already exists")
    else:
        print(f"[kibana] ERROR creating data view: {r.status_code} {r.text}")
        raise SystemExit(2)
    return r.json() if r.text else {}


# ── A small DSL for Lens visualisations ────────────────────────────────────
# These use the legacy "visualization" type with the visState string so we
# don't depend on Kibana version specific Lens schemas.

def _viz(viz_id: str, title: str, vis_type: str, vis_state: dict,
         description: str = "", query_kuery: str = "",
         coloured_by_sentiment: bool = False) -> dict:
    """Build a saved-object payload for a Kibana 'visualization' object.

    Pass `query_kuery` (e.g. `sentiment_label: "negative"`) to filter the
    viz to a subset of the index without needing a separate saved search.

    Set `coloured_by_sentiment=True` to bake in the red/blue/green palette
    for series labelled negative/neutral/positive.
    """
    return {
        "attributes": {
            "title":       title,
            "description": description,
            "visState":    json.dumps({"title": title, "type": vis_type, **vis_state}),
            "uiStateJSON": _UI_STATE_COLOURS if coloured_by_sentiment else "{}",
            "version":     1,
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "query":  {"query": query_kuery, "language": "kuery"},
                    "filter": [],
                    "indexRefName": "kibanaSavedObjectMeta.searchSourceJSON.index",
                }),
            },
        },
        "references": [{
            "name": "kibanaSavedObjectMeta.searchSourceJSON.index",
            "type": "index-pattern",
            "id":   DATA_VIEW_ID,
        }],
    }


# ── KPI metric cards ───────────────────────────────────────────────────────
def _metric_viz(viz_id: str, title: str, agg: dict,
                query_kuery: str = "",
                font_size: int = 60,
                description: str = "") -> tuple[str, dict]:
    """Big-number visualisation. `agg` is the single metric aggregation."""
    return viz_id, _viz(
        viz_id, title, "metric",
        description=description,
        query_kuery=query_kuery,
        vis_state={
            "aggs": [{**agg, "id": "1", "enabled": True, "schema": "metric"}],
            "params": {
                "addTooltip": True,
                "addLegend":  False,
                "type":       "metric",
                "metric": {
                    "percentageMode":  False,
                    "useRanges":       False,
                    "colorSchema":     "Green to Red",
                    "metricColorMode": "None",
                    "colorsRange":     [{"from": 0, "to": 10_000_000}],
                    "labels":          {"show": True},
                    "invertColors":    False,
                    "style": {
                        "bgFill":     "#000",
                        "bgColor":    False,
                        "labelColor": False,
                        "subText":    "",
                        "fontSize":   font_size,
                    },
                },
            },
        },
    )


def viz_card_total() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-total", "Total comments classified",
        {"type": "count", "params": {}},
        description="Total documents in youtube_sentiment index.")


def viz_card_videos() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-videos", "Unique videos",
        {"type": "cardinality", "params": {"field": "video_id"}},
        description="Distinct FUZZ CHANNEL videos in the stream.")


def viz_card_avg_score() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-avg-score", "Avg model confidence",
        {"type": "avg", "params": {"field": "sentiment_score"}},
        description="Average winning-class probability across all predictions.",
        font_size=50)


def viz_card_negative() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-negative", "Negative comments",
        {"type": "count", "params": {}},
        query_kuery='sentiment_label: "negative"',
        description="Count of documents classified as negative.")


def viz_card_neutral() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-neutral", "Neutral comments",
        {"type": "count", "params": {}},
        query_kuery='sentiment_label: "neutral"',
        description="Count of documents classified as neutral.")


def viz_card_positive() -> tuple[str, dict]:
    return _metric_viz(
        "viz-card-positive", "Positive comments",
        {"type": "count", "params": {}},
        query_kuery='sentiment_label: "positive"',
        description="Count of documents classified as positive.")


def viz_pie() -> tuple[str, dict]:
    return "viz-sentiment-pie", _viz(
        "viz-sentiment-pie",
        "Sentiment label distribution",
        "pie",
        description="Donut of negative / neutral / positive across all classified comments.",
        coloured_by_sentiment=True,
        vis_state={
            "aggs": [
                {"id": "1", "enabled": True, "type": "count",
                 "params": {}, "schema": "metric"},
                {"id": "2", "enabled": True, "type": "terms",
                 "params": {"field": "sentiment_label",
                            "orderBy": "1", "order": "desc",
                            "size": 3, "otherBucket": False,
                            "missingBucket": False},
                 "schema": "segment"},
            ],
            "params": {"type": "pie", "addTooltip": True, "addLegend": True,
                       "legendPosition": "right", "isDonut": True,
                       "labels": {"show": True, "values": True,
                                  "last_level": True, "truncate": 100}},
        },
    )


def viz_timeseries() -> tuple[str, dict]:
    return "viz-sentiment-timeseries", _viz(
        "viz-sentiment-timeseries",
        "Sentiment over time",
        "histogram",
        description="Stacked bars by published_at, broken down by sentiment.",
        coloured_by_sentiment=True,
        vis_state={
            "aggs": [
                {"id": "1", "enabled": True, "type": "count",
                 "params": {}, "schema": "metric"},
                {"id": "2", "enabled": True, "type": "date_histogram",
                 "params": {"field": "published_at",
                            "useNormalizedEsInterval": True,
                            "interval": "auto", "drop_partials": False,
                            "min_doc_count": 1, "extended_bounds": {}},
                 "schema": "segment"},
                {"id": "3", "enabled": True, "type": "terms",
                 "params": {"field": "sentiment_label", "orderBy": "1",
                            "order": "desc", "size": 3,
                            "otherBucket": False, "missingBucket": False},
                 "schema": "group"},
            ],
            "params": {
                "type": "histogram",
                "grid": {"categoryLines": False},
                "categoryAxes": [{"id": "CategoryAxis-1", "type": "category",
                                  "position": "bottom", "show": True,
                                  "scale": {"type": "linear"},
                                  "labels": {"show": True, "filter": True,
                                             "truncate": 100}, "title": {}}],
                "valueAxes":    [{"id": "ValueAxis-1", "name": "LeftAxis-1",
                                  "type": "value", "position": "left",
                                  "show": True,
                                  "scale": {"type": "linear", "mode": "normal"},
                                  "labels": {"show": True, "rotate": 0,
                                             "filter": False, "truncate": 100},
                                  "title": {"text": "Count"}}],
                "seriesParams": [{"show": True, "type": "histogram",
                                  "mode": "stacked",
                                  "data": {"label": "Count", "id": "1"},
                                  "valueAxis": "ValueAxis-1",
                                  "drawLinesBetweenPoints": True,
                                  "showCircles": True}],
                "addTooltip": True, "addLegend": True,
                "legendPosition": "right", "times": [], "addTimeMarker": False,
            },
        },
    )


def viz_top_videos() -> tuple[str, dict]:
    # Switched from horizontal_bar to a data table — long video titles can't fit
    # legibly on a bar chart's Y axis at dashboard size. A table puts each title
    # on its own row with the per-class counts as columns, which is both readable
    # and sortable.
    return "viz-top-videos", _viz(
        "viz-top-videos",
        "Top 10 videos by sentiment",
        "table",
        description="Table of the 10 most-discussed videos with counts per sentiment class.",
        coloured_by_sentiment=True,
        vis_state={
            "aggs": [
                {"id": "1", "enabled": True, "type": "count",
                 "params": {}, "schema": "metric"},
                {"id": "2", "enabled": True, "type": "terms",
                 "params": {"field": "video_title", "orderBy": "1",
                            "order": "desc", "size": 10,
                            "otherBucket": False, "missingBucket": False},
                 "schema": "bucket"},
                {"id": "3", "enabled": True, "type": "terms",
                 "params": {"field": "sentiment_label", "orderBy": "1",
                            "order": "desc", "size": 3,
                            "otherBucket": False, "missingBucket": False},
                 "schema": "bucket"},
            ],
            "params": {
                "perPage":                10,
                "percentageCol":          "",
                "row":                    True,
                "showMetricsAtAllLevels": False,
                "showPartialRows":        False,
                "showTotal":              True,
                "totalFunc":              "sum",
            },
        },
    )


def viz_wordcloud() -> tuple[str, dict]:
    # significant_terms requires a keyword/fielddata field — comment_text is a
    # plain text field so that aggregation errors out. significant_text is
    # designed for exactly this case (samples docs, picks distinctive terms in
    # a text field) and renders fine in the tag cloud visualisation.
    return "viz-wordcloud", _viz(
        "viz-wordcloud",
        "Comment word cloud",
        "tagcloud",
        description="Significant words in comment_text. Filter by sentiment_label for per-class word clouds.",
        vis_state={
            "aggs": [
                {"id": "1", "enabled": True, "type": "count",
                 "params": {}, "schema": "metric"},
                {"id": "2", "enabled": True, "type": "significant_text",
                 "params": {"field": "comment_text", "size": 60,
                            "filter_duplicate_text": True},
                 "schema": "segment"},
            ],
            "params": {"scale":       "linear",
                       "orientation": "single",
                       "minFontSize": 24,
                       "maxFontSize": 84,
                       "showLabel":   True},
        },
    )


# ── Dashboard ──────────────────────────────────────────────────────────────
def make_dashboard(panels: list[tuple[str, int, int, int, int]]) -> dict:
    """Build a dashboard saved object from a list of (viz_id, x, y, w, h) tuples.

    Grid is 48 columns wide (Kibana default). Cards in row 1 are 8 cols each
    (six fit). The big charts in rows 2/3 are 24 cols wide and 26 rows tall
    so axis labels, video titles and word-cloud terms have room to breathe.
    """
    panels_json = []
    refs = []
    for i, (vid, x, y, w, h) in enumerate(panels, start=1):
        panel_ref = f"panel_{i}"
        panels_json.append({
            "version":     "8.13.4",
            "type":        "visualization",
            "gridData":    {"x": x, "y": y, "w": w, "h": h, "i": str(i)},
            "panelIndex":  str(i),
            "embeddableConfig": {},
            "panelRefName": panel_ref,
        })
        refs.append({"name": panel_ref, "type": "visualization", "id": vid})
    return {
        "attributes": {
            "title":       "FUZZ CHANNEL Sentiment",
            "description": "Real-time sentiment dashboard fed by Kafka -> Spark -> Elasticsearch.",
            "panelsJSON":  json.dumps(panels_json),
            "optionsJSON": json.dumps({"hidePanelTitles": False, "useMargins": True,
                                       "syncColors": True, "syncCursor": True,
                                       "syncTooltips": True}),
            "version":     1,
            # Bake in a sensible default time window. FUZZ CHANNEL's comments
            # are concentrated in the last ~12 months, so opening the dashboard
            # with that range avoids huge empty space on the time-series panel.
            "timeRestore": True,
            "timeFrom":    "now-1y",
            "timeTo":      "now",
            "refreshInterval": {"pause": True, "value": 5000},
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({"query": {"language": "kuery", "query": ""},
                                                "filter": []}),
            },
        },
        "references": refs,
    }


def put_object(base: str, kind: str, obj_id: str, payload: dict,
               overwrite: bool) -> None:
    url = f"{base}/api/saved_objects/{kind}/{obj_id}"
    if overwrite:
        url += "?overwrite=true"
    r = requests.post(url, headers=HEADERS, data=json.dumps(payload))
    if r.status_code in (200, 201):
        print(f"[kibana] upserted {kind} '{obj_id}'")
    else:
        print(f"[kibana] ERROR upserting {kind}/{obj_id}: {r.status_code} {r.text}")
        raise SystemExit(3)


def delete_object(base: str, kind: str, obj_id: str) -> None:
    r = requests.delete(f"{base}/api/saved_objects/{kind}/{obj_id}",
                        headers=HEADERS)
    if r.status_code in (200, 204):
        print(f"[kibana] deleted {kind} '{obj_id}'")
    elif r.status_code == 404:
        print(f"[kibana] (no {kind} '{obj_id}' to delete)")
    else:
        print(f"[kibana] WARN deleting {kind}/{obj_id}: {r.status_code} {r.text}")


def main() -> int:
    p = argparse.ArgumentParser(description="Set up Kibana dashboard objects")
    p.add_argument("--host",   default=KIBANA_HOST)
    p.add_argument("--delete", action="store_true",
                   help="delete all dashboard objects first, then recreate")
    args = p.parse_args()

    # Wait for Kibana up
    try:
        r = requests.get(f"{args.host}/api/status", timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[kibana] ERROR: cannot reach Kibana at {args.host}: {e}")
        return 2

    # ── KPI cards (row 1) ──────────────────────────────────────────────
    cards = [viz_card_total, viz_card_videos, viz_card_avg_score,
             viz_card_negative, viz_card_neutral, viz_card_positive]
    # ── Existing charts (rows 2-3) ─────────────────────────────────────
    charts = [viz_pie, viz_timeseries, viz_top_videos, viz_wordcloud]

    if args.delete:
        delete_object(args.host, "dashboard", "fuzz-sentiment-dashboard")
        for builder in cards + charts:
            vid, _ = builder()
            delete_object(args.host, "visualization", vid)
        delete_object(args.host, "index-pattern", DATA_VIEW_ID)

    create_data_view(args.host)

    # Upsert every visualisation
    card_ids:  list[str] = []
    chart_ids: list[str] = []
    for builder in cards:
        vid, payload = builder()
        put_object(args.host, "visualization", vid, payload, overwrite=True)
        card_ids.append(vid)
    for builder in charts:
        vid, payload = builder()
        put_object(args.host, "visualization", vid, payload, overwrite=True)
        chart_ids.append(vid)

    # ── Dashboard layout (48-col grid) ─────────────────────────────────
    #   Row 1 (y=0,  h=10):  6 KPI cards   — 8 cols each, side by side
    #   Row 2 (y=10, h=26):  pie | timeseries
    #   Row 3 (y=36, h=26):  top videos | word cloud
    layout: list[tuple[str, int, int, int, int]] = []
    for i, cid in enumerate(card_ids):
        layout.append((cid, i * 8, 0, 8, 10))
    layout.append((chart_ids[0],  0, 10, 24, 26))   # pie
    layout.append((chart_ids[1], 24, 10, 24, 26))   # timeseries
    layout.append((chart_ids[2],  0, 36, 24, 26))   # top videos
    layout.append((chart_ids[3], 24, 36, 24, 26))   # word cloud

    put_object(args.host, "dashboard", "fuzz-sentiment-dashboard",
               make_dashboard(layout), overwrite=True)

    print()
    print("=" * 70)
    print(f"  Dashboard ready: {args.host}/app/dashboards#/view/fuzz-sentiment-dashboard")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
