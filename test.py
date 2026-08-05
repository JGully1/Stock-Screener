import yfinance as yf

stock = yf.Ticker("AAPL")
info = stock.info 

print(info)