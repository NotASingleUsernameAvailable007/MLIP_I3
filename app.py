from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

# Static list of movies for demonstration purposes
movie_recommendations = [
    "Inception",
    "The Matrix",
    "Parasite",
    "Interstellar",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "Fight Club",
    "The Shawshank Redemption"
]

# Function to analyze feedback
def analyze_feedback(feedback):
    blob = TextBlob(feedback)
    sentiment = blob.sentiment.polarity
    print(sentiment, "-----sentiment")
    return "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

@app.route('/', methods=['GET', 'POST'])
def home():
    feedback_type = None
    if request.method == 'POST':
        user_feedback = request.form['feedback']
        feedback_type = analyze_feedback(user_feedback)
    return render_template('index.html', feedback_type=feedback_type, movies=movie_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
