"use client"

import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from "recharts"
import { format, parseISO, startOfDay, subDays, isValid } from "date-fns"

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

interface SentimentChartProps {
  data: SentimentData[]
}

export function SentimentChart({ data }: SentimentChartProps) {
  const processChartData = () => {
    if (!data || data.length === 0) {
      return []
    }

    const now = new Date()
    const sevenDaysAgo = subDays(now, 7)

    // Create daily buckets instead of hourly for better visualization
    const dailyData = new Map()

    // Initialize buckets for the past 7 days
    for (let i = 0; i < 7; i++) {
      const day = startOfDay(subDays(now, 6 - i))
      const key = day.toISOString().split("T")[0] // Use YYYY-MM-DD format
      dailyData.set(key, {
        date: key,
        positive: 0,
        negative: 0,
        neutral: 0,
        total: 0,
      })
    }

    // Group actual data by day
    data.forEach((item) => {
      let itemDate: Date

      // Handle both Unix timestamp and ISO string
      if (typeof item.created_utc === "number") {
        itemDate = new Date(item.created_utc * 1000)
      } else {
        // Try parsing processed_at if created_utc is not valid
        itemDate = parseISO(item.processed_at)
      }

      // Validate the date
      if (!isValid(itemDate)) {
        console.warn("Invalid date for item:", item)
        return
      }

      if (itemDate >= sevenDaysAgo) {
        const dayKey = startOfDay(itemDate).toISOString().split("T")[0]
        const bucket = dailyData.get(dayKey)
        if (bucket) {
          bucket[item.sentiment]++
          bucket.total++
        }
      }
    })

    const result = Array.from(dailyData.values()).sort(
      (a, b) => new Date(a.date).getTime() - new Date(b.date).getTime(),
    )

    console.log("Chart data:", result) // Debug log
    return result
  }

  const chartData = processChartData()

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 border rounded-lg shadow-lg">
          <p className="font-medium">{format(new Date(label), "MMM dd, yyyy")}</p>
          {payload.map((entry: any, index: number) => (
            <p key={index} style={{ color: entry.color }} className="text-sm">
              {`${entry.name}: ${entry.value}`}
            </p>
          ))}
        </div>
      )
    }
    return null
  }

  // If no data, show a message
  if (chartData.length === 0 || chartData.every((d) => d.total === 0)) {
    return (
      <div className="h-80 flex items-center justify-center text-gray-500">
        <div className="text-center">
          <p className="text-lg font-medium">No time-series data available</p>
          <p className="text-sm">Data will appear here as more comments are processed over time</p>
        </div>
      </div>
    )
  }

  return (
    <div className="h-80">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={chartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" className="opacity-30" />
          <XAxis dataKey="date" tickFormatter={(value) => format(new Date(value), "MM/dd")} className="text-xs" />
          <YAxis className="text-xs" />
          <Tooltip content={<CustomTooltip />} />
          <Legend />
          <Line
            type="monotone"
            dataKey="positive"
            stroke="#10b981"
            strokeWidth={2}
            name="Positive"
            dot={{ r: 4 }}
            connectNulls={false}
          />
          <Line
            type="monotone"
            dataKey="negative"
            stroke="#ef4444"
            strokeWidth={2}
            name="Negative"
            dot={{ r: 4 }}
            connectNulls={false}
          />
          <Line
            type="monotone"
            dataKey="neutral"
            stroke="#6b7280"
            strokeWidth={2}
            name="Neutral"
            dot={{ r: 4 }}
            connectNulls={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
