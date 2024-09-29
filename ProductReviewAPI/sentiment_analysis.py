import pandas as pd
from textblob import TextBlob

def analyze_sentiment(file_path):
    df = pd.read_csv(file_path)
    df['Sentiment'] = df['Review Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['Sentiment Class'] = df['Sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
    df.to_csv('iphone_12_reviews_with_sentiment.csv', index=False)

if __name__ == '__main__':
    analyze_sentiment('iphone_12_reviews.csv')
