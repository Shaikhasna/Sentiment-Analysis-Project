from flask import Flask, render_template, request

app = Flask(__name__)

# Function to analyze sentiment (example code)
def analyze_sentiment(text):
    # Basic sentiment analysis logic
    text = text.lower()
    if "love" in text or "great" in text or "awesome" in text:
        return "Positive"
    elif "hate" in text or "worst" in text or "bad" in text:
        return "Negative"
    else:
        return "Neutral"

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    if request.method == "POST":
        # Get the text from the form
        text = request.form["text"]
        # Perform sentiment analysis
        sentiment = analyze_sentiment(text)
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
