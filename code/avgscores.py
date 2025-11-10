import pandas as pd

# Load the already-cleaned dataset (produced by cleaning.process_reddit)
input_csv = './datasets/cleaned_wallstreetbets_dataset_with_sentiments.csv'
df = pd.read_csv(input_csv)

print("Original dataset (cleaned input):")
print(df.info())

# Calculate the average sentiment score of Vader for each day
df_grouped = df.groupby('formatted_date')['sentiment_vader'].mean()

# Save the average sentiment scores of VADER by day
sentiment_scores_by_day_file_path = './code/sentiment_scores_by_day_vader.csv'
df_grouped.to_csv(sentiment_scores_by_day_file_path, index=True)

print("\nAverage sentiment scores of VADER by day:")
print(df_grouped.info())
print(df_grouped.head())

