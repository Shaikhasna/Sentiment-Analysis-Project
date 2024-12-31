import sys
import os

# Add the src directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import the analyze_sentiment function
from sentiment_analysis import analyze_sentiment


def test_analyze_sentiment():
    # Positive sentiment
    assert analyze_sentiment("I love it!") == "Positive"
    
    # Negative sentiment
    assert analyze_sentiment("I hate it!") == "Negative"
    
    # Neutral sentiment
    assert analyze_sentiment("It's okay.") == "Neutral"  # This should pass if the logic handles neutral sentiments
