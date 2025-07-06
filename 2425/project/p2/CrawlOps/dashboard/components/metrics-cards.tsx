import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, TrendingDown, Minus, Activity } from "lucide-react"
import { Skeleton } from "@/components/ui/skeleton"

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

interface MetricsCardsProps {
  data: SentimentData[]
  isLoading: boolean
}

export function MetricsCards({ data, isLoading }: MetricsCardsProps) {
  if (isLoading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {Array.from({ length: 4 }).map((_, i) => (
          <Card key={i}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <Skeleton className="h-4 w-20" />
              <Skeleton className="h-4 w-4" />
            </CardHeader>
            <CardContent>
              <Skeleton className="h-8 w-16 mb-2" />
              <Skeleton className="h-3 w-24" />
            </CardContent>
          </Card>
        ))}
      </div>
    )
  }

  const totalCount = data.length
  const positiveCount = data.filter((d) => d.sentiment === "positive").length
  const negativeCount = data.filter((d) => d.sentiment === "negative").length
  const neutralCount = data.filter((d) => d.sentiment === "neutral").length

  const avgConfidence =
    data.length > 0 ? ((data.reduce((sum, d) => sum + d.sentiment_score, 0) / data.length) * 100).toFixed(1) : "0"

  const positivePercentage = totalCount > 0 ? ((positiveCount / totalCount) * 100).toFixed(1) : "0"
  const negativePercentage = totalCount > 0 ? ((negativeCount / totalCount) * 100).toFixed(1) : "0"
  const neutralPercentage = totalCount > 0 ? ((neutralCount / totalCount) * 100).toFixed(1) : "0"

  const metrics = [
    {
      title: "Total Analyzed",
      value: totalCount.toLocaleString(),
      description: "Total texts processed",
      icon: Activity,
      color: "text-blue-600",
    },
    {
      title: "Positive Sentiment",
      value: `${positivePercentage}%`,
      description: `${positiveCount.toLocaleString()} positive texts`,
      icon: TrendingUp,
      color: "text-green-600",
    },
    {
      title: "Negative Sentiment",
      value: `${negativePercentage}%`,
      description: `${negativeCount.toLocaleString()} negative texts`,
      icon: TrendingDown,
      color: "text-red-600",
    },
    {
      title: "Average Confidence",
      value: `${avgConfidence}%`,
      description: "Model prediction confidence",
      icon: Minus,
      color: "text-purple-600",
    },
  ]

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {metrics.map((metric, index) => (
        <Card key={index}>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-gray-600">{metric.title}</CardTitle>
            <metric.icon className={`h-4 w-4 ${metric.color}`} />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{metric.value}</div>
            <p className="text-xs text-gray-500 mt-1">{metric.description}</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
