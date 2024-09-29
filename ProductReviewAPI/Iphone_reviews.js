import React, { useEffect, useState } from 'react';

export default function Iphone_review() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/reviews') // Update this URL if necessary
      .then(response => response.json())
      .then(data => setReviews(data))
      .catch(error => console.error('Error fetching reviews:', error));
  }, []);

  return (
    <div className="review-container">
      <h1>iPhone 12 Reviews</h1>
      
      <div className="filter-section">
        {/* Add filter dropdowns here */}
      </div>

      <div className="reviews">
        {reviews.map((review, index) => (
          <div key={index} className="review-card box1">
            <h2>{review['Review Title']}</h2>
            <p>{review['Review Text']}</p>
            <p className="meta">Storage: {review['Storage Size']} | Color: {review['Colour']}</p>
          </div>
        ))}
      </div>

      <div className="review-card box2">
        <h2>Additional Insights</h2>
        <p>This section can be used for any extra information or promotions!</p>
      </div>
    </div>
  );
}
