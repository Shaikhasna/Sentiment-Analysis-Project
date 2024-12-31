from textblob import TextBlob
import pandas as pd

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Convert text to lowercase for uniformity
    text = text.lower()

    # Check for common positive, negative, or neutral phrases
    if "love" in text or "great" in text or "awesome" in text:
        return "Positive"
    elif "hate" in text or "worst" in text or "bad" in text:
        return "Negative"
    elif "okay" in text or "fine" in text or "average" in text:
        return "Neutral"
    else:
        # Use TextBlob for more granular sentiment analysis if no clear keyword is found
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"  # Default case for neutral sentiment


# Function to process a list of texts
def process_sentiment_analysis(texts):
    results = []
    for text in texts:
        sentiment = analyze_sentiment(text)
        results.append((text, sentiment))
    return results

# Example usage with some sample text (you can replace this with actual data)
if __name__ == "__main__":
    sample_texts = [
        "I love the new design of this app!",
        "This is the worst experience I have had.",
        "The product is okay, not great but not bad either.",
        "The food was amazing, will definitely come again.",
        "I feel horrible after the meeting today."
    ]
    
    # Perform sentiment analysis on each sample text
    sentiment_results = process_sentiment_analysis(sample_texts)

    # Display results in a more user-friendly format
    print("Sentiment Analysis Results:\n")
    for text, sentiment in sentiment_results:
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment}")
        print("------")
