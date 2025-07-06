import { Badge } from "@/components/ui/badge"
import { Card } from "@/components/ui/card"
import { formatDistanceToNow } from "date-fns"

interface SentimentData {
  id: string
  body: string
  author: string
  created_utc: number
  subreddit: string
  sentiment: "positive" | "negative" | "neutral"
  sentiment_score: number
  processed_at: string
}

interface RecentAnalysisProps {
  data: SentimentData[]
}

export function RecentAnalysis({ data }: RecentAnalysisProps) {
  const getSentimentColor = (sentiment: string) => {
    switch (sentiment) {
      case "positive":
        return "bg-green-100 text-green-800 border-green-200"
      case "negative":
        return "bg-red-100 text-red-800 border-red-200"
      case "neutral":
        return "bg-gray-100 text-gray-800 border-gray-200"
      default:
        return "bg-gray-100 text-gray-800 border-gray-200"
    }
  }

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 0.8) return "text-green-600"
    if (confidence >= 0.6) return "text-yellow-600"
    return "text-red-600"
  }

  if (data.length === 0) {
    return <div className="text-center py-8 text-gray-500">No recent analysis data available</div>
  }

  return (
    <div className="space-y-3 max-h-96 overflow-y-auto">
      {data.map((item) => (
        <Card key={item.id} className="p-4 hover:shadow-md transition-shadow">
          <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-3">
            <div className="flex-1 min-w-0">
              <p className="text-sm text-gray-900 line-clamp-2 mb-2">{item.body}</p>
              <div className="flex flex-wrap items-center gap-2 text-xs text-gray-500">
                <span>{formatDistanceToNow(new Date(item.created_utc * 1000), { addSuffix: true })}</span>
                <span>•</span>
                <span>r/{item.subreddit}</span>
                <span>•</span>
                <span>u/{item.author}</span>
              </div>
            </div>
            <div className="flex items-center gap-2 flex-shrink-0">
              <Badge variant="outline" className={getSentimentColor(item.sentiment)}>
                {item.sentiment}
              </Badge>
              <span className={`text-xs font-medium ${getConfidenceColor(item.sentiment_score)}`}>
                {(item.sentiment_score * 100).toFixed(0)}%
              </span>
            </div>
          </div>
        </Card>
      ))}
    </div>
  )
}
