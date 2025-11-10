import pandas as pd
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Load sentiment scores
sentiment_scores_df = pd.read_csv('./code/sentiment_scores_by_day_vader.csv')

# Load stock data
stock_data_df = pd.read_csv('./datasets/GME.csv')
merged_df = sentiment_scores_df.merge(stock_data_df, on='formatted_date')
correlation = merged_df['sentiment_vader'].corr(merged_df['Open'])
print("Correlation between sentiment score and Open price:", correlation)
positive_sentiment_returns = merged_df[merged_df['sentiment_vader'] > 0]['Open'].pct_change()

print("Average returns for positive sentiment days:", positive_sentiment_returns.mean())
plt.scatter(merged_df['sentiment_vader'], merged_df['Open'])
plt.xlabel('Sentiment Score')
plt.ylabel('Open Price')
plt.title('Sentiment Score vs. Open Price')
plt.show()
plt.plot(merged_df['formatted_date'], merged_df['sentiment_vader'], label='sentiment_vader')
plt.plot(merged_df['formatted_date'], merged_df['Open'], label='Open Price')
plt.xlabel('formatted_date')
plt.ylabel('Value')
plt.title('Sentiment Score and Open Price Time Series')
plt.legend()
plt.show()

