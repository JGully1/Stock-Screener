import pandas as pd 
import streamlit as st 


@st.cache_data
def load_data():
    df = pd.read_csv('sp500_stock_screener.csv')
    numeric_columns = ['Market Cap (USD)', 'P/E Ratio', 'Dividend Yield']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

screener_df = load_data()
st.dataframe(screener_df)

def rank_stocks(df, column, ascending=False,top_n=20):
    df['Rank'] = df[column].rank(ascending=ascending,method='min')
    ranked_df = df.sort_values(by='Rank').head(top_n)
    return ranked_df[['Rank', 'Ticker', 'Company Name', column, 'Market']]

st.title("S&P 500 Stock Screener")
st.sidebar.header('User Options')

# If you want to add a market filter, you can uncomment the following lines and ensure that the 'Market' column exists in your screener_df DataFrame.
# markets = screener_df['Market'].unique()
# selected_market = st.sidebar.multiselect('Select Markets', markets, default=markets)

