import pandas as pd 
import yfinance as yf
import time

# Load the tickers from a CSV file, add as needed
tickers_df = pd.read_csv('sp500_companies.csv')

screener_data = []

# Loop through each ticker and fetch data from Yahoo Finance
for ticker in tickers_df['Symbol']:
    print(f'Fetching data for {ticker}')
    stock = yf.Ticker(ticker)
    info = stock.info

    screener_data.append({
        'Ticker': ticker,
        'Company Name': info.get('longName', 'N/A'),
        'Market Cap (USD)': info.get('marketCap', 'N/A'),
        'P/E Ratio': info.get('trailingPE', 'N/A'),
        'Dividend Yield': info.get('dividendYield', 'N/A'),
        'Sector': info.get('sector', 'N/A'),
        'Industry': info.get('industry', 'N/A'),
        'Currency': info.get('currency', 'USD'),
    })
    time.sleep(1)  # To avoid hitting API rate limits

screener_df = pd.DataFrame(screener_data)

numeric_columns = ['Market Cap (USD)', 'P/E Ratio', 'Dividend Yield']

for col in numeric_columns:
    screener_df[col] = pd.to_numeric(screener_df[col], errors='coerce')

# Currently Market Cap is in USD, but if other companies are in different currencies, you may need to convert them to USD using exchange rates.

screener_df.to_csv('sp500_stock_screener.csv', index=False)  # Save the data to a CSV file for later use

def rank_stocks(df, column, ascending=False,top_n=20):
    df['Rank'] = df[column].rank(ascending=ascending,method='min')
    ranked_df = df.sort_values(by='Rank').head(top_n)
    return ranked_df[['Rank', 'Ticker', 'Company Name', column]]

#This function can be used in the dashboard.py to rank stocks based on a specific column and display the top N stocks. For example, you can call: 
rank_stocks(screener_df, column='Market Cap (USD)', ascending=False, top_n=10)
