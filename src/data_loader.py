import pandas as pd

def load_data():
    goldbees_df = pd.read_csv('../data/goldbees_4yr_data.csv', parse_dates=True, index_col='Date')
    hdfc_gold_df = pd.read_csv('../data/hdfcgold_4yr_data.csv', parse_dates=True, index_col='Date')
    return goldbees_df, hdfc_gold_df
import yfinance as yf
import pandas as pd
from datetime import datetime

# Define tickers
goldbees = "GOLDBEES.NS"
hdfc_gold = "HDFCGOLD.NS"

# Date range: last 4 years
end_date = datetime.now().date()
start_date = end_date.replace(year=end_date.year - 4)

# Fetch data
goldbees_df = yf.download(goldbees, start=start_date, end=end_date)
hdfc_df = yf.download(hdfc_gold, start=start_date, end=end_date)

# Save to CSV
goldbees_df.to_csv('../data/goldbees_4yr_data.csv')
hdfc_df.to_csv('../data/hdfcgold_4yr_data.csv')

print("✅ GoldBees and HDFC Gold ETF data saved successfully!")