from cleaning import process_reddit

if __name__ == '__main__':
    process_reddit(
        input_csv="./output/reddit-posts.csv",
        output_csv="./datasets/cleaned_wallstreetbets_dataset_with_sentiments1.csv",
        tickers=["gme"]
    )

