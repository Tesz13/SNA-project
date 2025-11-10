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

## Setup Instructions

### Prerequisites

- **Python 3.8 or higher** - Download from [python.org](https://www.python.org/downloads/) or Microsoft Store
- **Windows PowerShell** (or compatible terminal)
- **Git** - Download from [git-scm.com](https://git-scm.com/downloads) (required for cloning)

### Step 1: Clone the Repository

If you're setting up the project from GitHub, clone it first:

1. **Using HTTPS (recommended):**
   ```powershell
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Using SSH (if you have SSH keys set up):**
   ```powershell
   git clone git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

3. **Download as ZIP (alternative):**
   - Go to your GitHub repository
   - Click the green "Code" button
   - Select "Download ZIP"
   - Extract the ZIP file to your desired location
   - Navigate to the extracted folder in PowerShell

**Note**: Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repository name.

### Step 2: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/windows/) or install from Microsoft Store
2. **Important**: During installation, check the box **"Add python.exe to PATH"**
3. Verify installation by opening PowerShell and running:
   ```powershell
   py --version
   ```
   or
   ```powershell
   python --version
   ```

### Step 3: Navigate to Project Directory

Open PowerShell and navigate to the project folder (if you cloned it, you're already in the right directory):
```powershell
cd YOUR_REPO_NAME
```

Or if you downloaded/extracted the project manually:
```powershell
cd "path\to\your\project\folder"
```

### Step 4: Create Virtual Environment

Create a virtual environment to isolate project dependencies:
```powershell
py -3 -m venv .venv
```

### Step 5: Activate Virtual Environment

Activate the virtual environment:
```powershell
Set-ExecutionPolicy -Scope Process RemoteSigned
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the beginning of your prompt, indicating the virtual environment is active.

**Note**: If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 6: Install Dependencies

Install all required Python packages:
```powershell
py -m pip install -r requirements.txt
```

This will install:
- pandas
- numpy
- scipy
- networkx
- matplotlib
- textblob
- nltk
- praw

### Step 7: Download NLTK and TextBlob Data

Download required language data for sentiment analysis:
```powershell
py -c "import nltk; nltk.download('vader_lexicon')"
py -m textblob.download_corpora
```

### Step 8: Verify Required Data Files

Ensure you have the following data files in place:

- **`output/reddit-posts.csv`** - Reddit posts dataset
- **`datasets/GME.csv`** - GameStop stock price data

For network analysis scripts, you may also need:
- **`datasets/congress.edgelist`** - For HITS/SALSA analysis
- **`datasets/lastfm_asia_edges.csv`** - For Girvan-Newman analysis

**Important**: If these data files are not included in the repository (due to size limitations), you'll need to:
1. Download them from the original sources (see Data Sources section above)
2. Place them in the appropriate folders (`output/` and `datasets/`)
3. Ensure the file names match exactly as listed above

### Step 9: Run the Scripts

Execute scripts in the following order:

1. **Clean and process Reddit data:**
   ```powershell
   py .\code\cleaning.py
   ```

2. **Calculate daily average sentiment:**
   ```powershell
   py .\code\avgscores.py
   ```

3. **Analyze sentiment vs stock prices:**
   ```powershell
   py .\code\stockandsentiment.py
   ```

4. **Analyze sentiment vs open prices (optional):**
   ```powershell
   py .\code\stocksentimentopen.py
   ```

### Troubleshooting

#### "Python is not recognized"
- Make sure Python is installed and added to PATH
- Try using `py` instead of `python` on Windows
- Restart your terminal after installing Python

#### "Activation script cannot be loaded"
- Run: `Set-ExecutionPolicy -Scope Process RemoteSigned`
- Then activate: `.\.venv\Scripts\Activate.ps1`

#### "Module not found"
- Ensure virtual environment is activated (you should see `(.venv)` in prompt)
- Reinstall dependencies: `py -m pip install -r requirements.txt`

#### "File not found" errors
- Make sure you're in the project root directory
- Verify required CSV files exist in `output/` and `datasets/` folders

#### NLTK/TextBlob data missing
- Re-run the download commands:
  ```powershell
  py -c "import nltk; nltk.download('vader_lexicon')"
  py -m textblob.download_corpora
  ```

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