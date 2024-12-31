import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Replace with your own Reddit app credentials
CLIENT_ID = 'JJ3gtLRdS7wW0bJs3wV-9g'
CLIENT_SECRET = 'okE9n4aa5O_qvoxvg9Z_XcK18X58lw'
USER_AGENT = 'SentimentAnalysisApp'

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Example: Fetch top posts from a subreddit (e.g., 'community')
subreddit = reddit.subreddit('community')  # Change this to your desired subreddit
for submission in subreddit.top(limit=10):  # Fetch top 10 posts
    title = submission.title
    url = submission.url
    score = submission.score

    # Analyze sentiment of the title
    sentiment_score = analyzer.polarity_scores(title)
    sentiment = 'Positive' if sentiment_score['compound'] > 0 else 'Negative' if sentiment_score['compound'] < 0 else 'Neutral'

    # Print the post's details and sentiment
    print(f"Title: {title}")
    print(f"URL: {url}")
    print(f"Score: {score}")
    print(f"Sentiment: {sentiment}")
    print()
