import pandas as pd 
import streamlit as st 

@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    numeric_columns = ['Market Cap (USD)', 'P/E Ratio', 'Dividend Yield']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

screener_df = load_data()
st.dataframe(screener_df)