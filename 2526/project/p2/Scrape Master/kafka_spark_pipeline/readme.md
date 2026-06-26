

# kafka_spark_pipeline/

This folder contains the streaming infrastructure of the project. Every file in here is part of the **real-time path** that moves a comment from the cleaned CSV all the way to the Kibana dashboard. The notebooks, the trained models, and the report figures live elsewhere in the repository.

## What is inside this folder

| File / Folder | What it does |
|---|---|
| **`docker-compose.yml`** | Defines the four supporting services — Kafka, Zookeeper, Elasticsearch, and Kibana — as Docker containers. Bringing up the whole stack is a single command (`docker compose up -d`). A named volume is declared for Elasticsearch so the indexed data survives container restarts. |
| **`producer.py`** | Reads the cleaned data file row by row, wraps each row in a JSON message, and publishes it to the Kafka topic `youtube-comments-raw`. The send rate is configurable, and the script can loop forever for demonstrations. |
| **`spark_streaming.py`** | The main streaming application. It subscribes to the Kafka topic, parses each JSON message, runs the soft-voting ensemble model on every five-second micro-batch, and writes the enriched documents to Elasticsearch in bulk. |
| **`es_setup.py`** | Creates the Elasticsearch index template before any data is written. The template defines explicit field types (keyword, text, date, float) so that Kibana aggregations work correctly. |
| **`elastic_mappings.json`** | The standalone JSON copy of the index mapping that `es_setup.py` applies. Provided as a separate artefact for reviewers who want to inspect the schema without reading Python code. |
| **`kibana_setup.py`** | Builds the Kibana dashboard through the Kibana REST API. It creates the data view, the six KPI cards, the four interactive visualisations, and the dashboard that contains them, all with a fixed red, blue, and green colour palette for the three sentiment classes. |
| **`dashboard/`** | Holds a saved-objects export of the Kibana dashboard (`.ndjson`), kept as a backup import path in case the REST API setup needs to be skipped. |
| **`figures/`** | Holds dashboard screenshots and other images that are embedded into the report and the main repository README. |


## Suggested run order

After bringing up Docker with `docker compose up -d`, the files are executed in this order:

1. `python es_setup.py` — create the Elasticsearch index template (once per fresh stack).
2. `python kibana_setup.py` — create the Kibana data view, panels, and dashboard (once per fresh stack).
3. `python spark_streaming.py` — start the streaming consumer; leave it running.
4. `python producer.py --rate 100 --loop` — start the producer; leave it running.

Once both `spark_streaming.py` and `producer.py` are running, the dashboard at `http://localhost:5601/app/dashboards#/view/fuzz-sentiment-dashboard` will begin to update in near real time.

---

Tell me if you also want short README files for the `dashboard/` and `figures/` subfolders, or a top-level GitHub README that links to this one.
