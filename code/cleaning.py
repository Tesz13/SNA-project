import pandas as pd
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def process_reddit(input_csv: str = "./output/reddit-posts.csv",
                   output_csv: str = "./datasets/cleaned_wallstreetbets_dataset_with_sentiments.csv",
                   tickers=None) -> pd.DataFrame:
    if tickers is None:
        tickers = ["gme"]

    df = pd.read_csv(input_csv)

    print("Original dataset:")
    print(df.info())

    df = df.drop_duplicates()
    df = df.dropna(subset=['title'])
    df['title'] = df['title'].str.lower()

    df['sentiment_textblob'] = df['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

    sia = SentimentIntensityAnalyzer()
    df['sentiment_vader'] = df['title'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

    for ticker in tickers:
        ticker_lower = str(ticker).lower()
        df[f'sentiment_{ticker_lower}'] = df['title'].apply(
            lambda x: str(x).count(ticker_lower) if pd.notnull(x) else 0
        )

    df.to_csv(output_csv, index=False)

    print("\nCleaned dataset with sentiment scores:")
    print(df.info())
    preview_cols = ['formatted_date' if 'formatted_date' in df.columns else 'timestamp',
                    'title', 'sentiment_textblob', 'sentiment_vader']
    first_ticker_col = f"sentiment_{str(tickers[0]).lower()}" if tickers else None
    if first_ticker_col and first_ticker_col in df.columns:
        preview_cols.append(first_ticker_col)
    print(df[preview_cols].head())

    return df


if __name__ == '__main__':
    process_reddit()

