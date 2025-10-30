# SNA-project
Analyzing the Effect of Reddit Discussions on Stock Performance
# Sentiment Analysis of Reddit Discussions and Stock Market Movement

## Project Overview
This project examines the relationship between online investor sentiment on Reddit (specifically the r/WallStreetBets community) and stock price movements. The primary objective was to determine whether discussions and sentiment expressed in social media forums can influence stock market behavior.  

The study focuses on the January 2021 GameStop (GME) short-squeeze event, which gained global attention due to retail-investor-driven market volatility.

---

## Objectives
- Analyze sentiment from Reddit posts and compare it with stock price behavior.
- Extract ticker references from WallStreetBets posts and correlate them with stock closing prices.
- Assess whether positive or negative sentiment aligns with upward or downward market movement.

---

## Data Sources
| Dataset | Source |
|--------|--------|
Stock Market Data | Kaggle: jacksoncrow/stock-market-dataset  
Reddit WallStreetBets Data | Kaggle: unanimad/reddit-rwallstreetbets  

Both datasets were filtered and synchronized to match the GameStop stock timeline for January 2021.

---

## Tools and Technologies
| Category | Tools |
|---------|------|
Programming | Python  
Libraries | Pandas, NLTK (VADER), Regex  
Data Format | CSV  
Visualization | Matplotlib / Scatter Plot  

---

## Methodology

### 1. Data Collection
- Imported Reddit discussion data and historical stock price data.

### 2. Data Preprocessing
- Standardized timestamps to `YYYY-MM-DD` to align Reddit posts with trading days.
- Extracted ticker symbols from posts using regular expressions.
- Filtered valid tickers by comparing against an official ticker list.

### 3. Sentiment Analysis
- Applied NLTK’s `SentimentIntensityAnalyzer (VADER)` to compute sentiment scores.
- Categorized scores as negative, neutral, or positive.

### 4. Data Integration
- Merged sentiment data with corresponding stock closing prices using date and ticker labels.

### 5. Visualization and Analysis
- Used scatter plot visualization to evaluate correlation patterns between sentiment and stock price movements.

---

## Key Findings
- Positive Reddit sentiment often corresponded with upward movement in stock prices.
- Impact was most noticeable during high-attention market events, particularly during the GME short-squeeze.
- Sentiment alone did not consistently predict price changes; influence appears situational and amplified during periods of high social attention.
- Reddit discussions can temporarily influence trading behavior, but sentiment data alone should not be considered a standalone market indicator.

---

## Challenges
- Extensive data cleaning required to standardize timestamps and filter false ticker matches.
- Aligning Reddit posting times with stock trading hours.
- Heatmaps were initially considered but replaced with scatter plots due to clarity concerns.

---

## Conclusion
This analysis indicates that sentiment extracted from Reddit discussions can influence stock market movements during periods of heightened public interest. However, the effect is inconsistent and event-driven. Social media sentiment should be considered as a supplementary analytical factor rather than a sole indicator for trading decisions.

---

## Future Work
- Extend analysis to additional stocks and time periods
- Integrate machine learning models to predict price movement
- Incorporate real-time Reddit streaming data
- Use more advanced sentiment techniques (e.g., transformer-based NLP models)
- Build interactive dashboards for visualization




