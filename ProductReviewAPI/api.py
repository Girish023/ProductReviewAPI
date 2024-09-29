from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Function to load reviews from the CSV file
def load_reviews():
    try:
        df = pd.read_csv('iphone_12_reviews.csv')
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Endpoint to get reviews based on color and storage size
@app.route('/reviews', methods=['GET'])
def get_reviews():
    # Load reviews
    df = load_reviews()
    print(df)  # Debug: print the entire DataFrame
    
    # Get query parameters
    color = request.args.get('color')
    storage_size = request.args.get('storage_size')
    print(f"Received color: {color}, storage_size: {storage_size}")  # Debug: print parameters

    if color and storage_size:
        # Filter the DataFrame based on query parameters
        filtered_reviews = df[(df['Colour'] == color) & (df['Storage Size'] == storage_size)]
        print(filtered_reviews)  # Debug: print filtered results
    else:
        # If no parameters are provided, return all reviews
        filtered_reviews = df

    return jsonify(filtered_reviews.to_dict(orient='records'))

# Endpoint to analyze sentiment of a review
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    review = data.get('review')

    if not review:
        return jsonify({"error": "Review not provided"}), 400

    # Placeholder for sentiment analysis logic
    sentiment = "positive"  # Replace this with actual sentiment analysis
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
