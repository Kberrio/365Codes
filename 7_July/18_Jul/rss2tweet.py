import feedparser
import tweepy

TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_SECRET = 'your_twitter_access_secret'

RSS_FEED_URL = 'https://example.com/feed'

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

feed = feedparser.parse(RSS_FEED_URL)
latest_entry = feed.entries[0]

tweet = f"{latest_entry.title[:100]}... {latest_entry.link}"
api.update_status(tweet)
