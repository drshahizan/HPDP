"use client"

import { useState, useEffect } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { RefreshCw, TrendingUp, MessageSquare, BarChart3 } from "lucide-react"
import { SentimentChart } from "@/components/sentiment-chart"
import { SentimentDistribution } from "@/components/sentiment-distribution"
import { RecentAnalysis } from "@/components/recent-analysis"
import { MetricsCards } from "@/components/metrics-cards"
import { createClient } from "@supabase/supabase-js"

// Replace the supabase configuration
const supabaseUrl = "https://qavwgrhcqquyjcgdjedp.supabase.co"
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhdndncmhjcXF1eWpjZ2RqZWRwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE1NDMwNDcsImV4cCI6MjA2NzExOTA0N30.35MBkB2jyTCXcYWxXJJ1w8wJK1YDEQc2QIBjmfjqr1g"
const supabase = createClient(supabaseUrl, supabaseKey)

// Update the interface to match your table structure
interface SentimentData {
  id: string
  body: string // Reddit comment text
  author: string
  created_utc: number // Unix timestamp
  subreddit: string
  sentiment: "positive" | "negative" | "neutral"
  sentiment_score: number // Your confidence score
  processed_at: string
}

export default function Dashboard() {
  const [sentimentData, setSentimentData] = useState<SentimentData[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [lastUpdated, setLastUpdated] = useState<Date>(new Date())

  const fetchSentimentData = async () => {
    try {
      setIsLoading(true)
      const { data, error } = await supabase
        .from("reddit_comments")
        .select("*")
        .order("processed_at", { ascending: false })
        .limit(1000)

      if (error) {
        console.error("Error fetching data:", error)
        setSentimentData(generateMockData())
      } else {
        setSentimentData(data || [])
      }
      setLastUpdated(new Date())
    } catch (error) {
      console.error("Error:", error)
      setSentimentData(generateMockData())
    } finally {
      setIsLoading(false)
    }
  }

  const generateMockData = (): SentimentData[] => {
    const sentiments: ("positive" | "negative" | "neutral")[] = ["positive", "negative", "neutral"]
    const subreddits = ["malaysia", "malaysians", "kualalumpur", "penang", "johor"]
    const sampleBodies = [
      "Great product! Highly recommend it to everyone in Malaysia.",
      "Terrible service, very disappointed with the quality.",
      "The event was okay, nothing special but not bad either.",
      "Amazing experience in KL! Will definitely come back again.",
      "Poor customer support, took too long to respond.",
      "Average quality for the price point in Malaysia.",
      "Excellent value for money, very satisfied with this Malaysian brand!",
      "Not worth the hype, expected much better from local companies.",
      "Decent product, meets basic expectations.",
      "Outstanding service and quality from this Malaysian company!",
    ]

    return Array.from({ length: 100 }, (_, i) => ({
      id: `mock-${i}`,
      body: sampleBodies[Math.floor(Math.random() * sampleBodies.length)],
      author: `user${Math.floor(Math.random() * 1000)}`,
      created_utc: Math.floor((Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000) / 1000),
      subreddit: subreddits[Math.floor(Math.random() * subreddits.length)],
      sentiment: sentiments[Math.floor(Math.random() * sentiments.length)],
      sentiment_score: Math.random() * 0.4 + 0.6,
      processed_at: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000).toISOString(),
    }))
  }

  useEffect(() => {
    fetchSentimentData()

    const subscription = supabase
      .channel("sentiment_changes")
      .on("postgres_changes", { event: "*", schema: "public", table: "reddit_comments" }, () => {
        fetchSentimentData()
      })
      .subscribe()

    // Refresh data every 30 seconds
    const interval = setInterval(fetchSentimentData, 30000)

    return () => {
      subscription.unsubscribe()
      clearInterval(interval)
    }
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-7xl mx-auto space-y-6">
        {/* Header */}
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Real-Time Sentiment Analysis Dashboard</h1>
            <p className="text-gray-600 mt-2">Monitoring Malaysian social media and review sentiment in real-time</p>
          </div>
          <div className="flex items-center gap-3">
            <Badge variant="outline" className="text-sm">
              Last updated: {lastUpdated.toLocaleTimeString()}
            </Badge>
            <Button onClick={fetchSentimentData} disabled={isLoading} size="sm" className="gap-2">
              <RefreshCw className={`h-4 w-4 ${isLoading ? "animate-spin" : ""}`} />
              Refresh
            </Button>
          </div>
        </div>

        {/* Metrics Cards */}
        <MetricsCards data={sentimentData} isLoading={isLoading} />

        {/* Charts Row */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <TrendingUp className="h-5 w-5" />
                Sentiment Trends Over Time
              </CardTitle>
              <CardDescription>Real-time sentiment analysis results from the past 7 days</CardDescription>
            </CardHeader>
            <CardContent>
              <SentimentChart data={sentimentData} />
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <BarChart3 className="h-5 w-5" />
                Sentiment Distribution
              </CardTitle>
              <CardDescription>Overall sentiment breakdown across all sources</CardDescription>
            </CardHeader>
            <CardContent>
              <SentimentDistribution data={sentimentData} />
            </CardContent>
          </Card>
        </div>

        {/* Recent Analysis */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <MessageSquare className="h-5 w-5" />
              Recent Sentiment Analysis
            </CardTitle>
            <CardDescription>Latest processed texts and their sentiment classifications</CardDescription>
          </CardHeader>
          <CardContent>
            <RecentAnalysis data={sentimentData.slice(0, 20)} />
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
