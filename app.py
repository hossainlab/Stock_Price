import yfinance as yf 
import pandas as pd 
import streamlit as st 

st.write("""
# Simple Stock Price App 

Shown are the closing price and volume of Google! 
"""
)

ticker_sumbol = "GOOGL"
ticker_data = yf.Ticker(ticker_sumbol)
ticker_df = ticker_data.history(period='id', start='2010-05-31', end='2020-5-31')

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume) 
