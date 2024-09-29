# ProductReviewAPI

This project is a Flask-based API that serves reviews for various products, starting with the iPhone 12. It provides endpoints to retrieve reviews based on color and storage size, as well as to analyze the sentiment of a given review.

## Description

The ProductReviewAPI is designed to help users access and analyze customer feedback on a variety of products. The API allows users to filter reviews by specific attributes such as color and storage size, making it easier to find relevant information. Additionally, it offers a basic sentiment analysis feature to gauge the overall sentiment expressed in a review.

### Key Features

- **Retrieve Reviews**: Users can fetch reviews from a CSV file filtered by specific parameters (color and storage size). This helps in understanding user preferences and experiences based on different configurations of products.
  
- **Sentiment Analysis**: Users can submit a review to receive a basic sentiment analysis result. This feature can be expanded with more sophisticated sentiment analysis algorithms in the future.

## Requirements

- Python 3.6+
- Flask
- Flask-CORS
- Pandas

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Girish023/ProductReviewAPI.git
   cd ProductReviewAPI
   ```

2. Install the required packages:

   ```bash
   pip install Flask Flask-CORS pandas
   ```

3. Ensure you have the `iphone_12_reviews.csv` file in the same directory as the application.

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

   The API will be available at `http://localhost:8000`.

2. **Get Reviews**

   To retrieve reviews, send a GET request to `/reviews` with optional query parameters for `color` and `storage_size`. 

   Example:

   ```bash
   curl "http://localhost:8000/reviews?color=Black&storage_size=64GB"
   ```

   If no parameters are provided, all reviews will be returned.

3. **Analyze Sentiment**

   To analyze the sentiment of a review, send a POST request to `/analyze` with a JSON body containing the review text.

   Example:

   ```bash
   curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"review": "I love my new iPhone!"}'
   ```

   The response will include the sentiment analysis result.

## Example Responses

1. **Get Reviews Response:**

   ```json
   [
       {
           "Review": "Great phone!",
           "Colour": "Black",
           "Storage Size": "64GB",
           "Rating": 5
       },
       ...
   ]
   ```

2. **Analyze Sentiment Response:**

   ```json
   {
       "sentiment": "positive"
   }
   ```

## Notes

- The sentiment analysis functionality is currently a placeholder and always returns "positive." You can replace it with actual sentiment analysis logic as needed.
- CORS is enabled for all origins, allowing for easy integration with frontend applications.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
