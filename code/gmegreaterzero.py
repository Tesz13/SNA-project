import pandas as pd
from cleaning import process_reddit

if __name__ == '__main__':
    df = process_reddit(
        input_csv="./output/reddit-posts.csv",
        output_csv="./datasets/cleaned_wallstreetbets_dataset_with_sentiments.csv",
        tickers=["gme"]
    )

    df_filtered = df[df['sentiment_gme'] > 0]
    filtered_file_path = './datasets/filtered_reddit-posts_with_sentiment_gme1.csv'
    df_filtered.to_csv(filtered_file_path, index=False)

    print("\nFiltered dataset with sentiment_gme>0:")
    print(df_filtered.info())
    print(df_filtered[['formatted_date', 'title', 'sentiment_textblob', 'sentiment_vader', 'sentiment_gme']].head())

