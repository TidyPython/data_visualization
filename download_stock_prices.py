import pandas as pd
import yfinance as yf


FinTech_tickers=pd.read_csv("ticker.csv")
print(FinTech_tickers)


def download_most_recent_price(ticker_new):
    data=yf.download(
        tickers=ticker_new,
        period="1d",
        interval="1d",
        auto_adjust=True,
        prepost=True,
        threads=True,
        proxy=None
    )
    data=data.reset_index()
    data["Ticker_name"]=ticker_new
    data_new=pd.DataFrame({
        'Ticker':ticker_new,
        'Date':data["Date"],
        'Close_price':data["Close"]
    })
    return(data_new)

df_combined = pd.DataFrame()


for index, row in FinTech_tickers.iterrows():
    df_tempt=download_most_recent_price(row['Ticker'])
    df_combined=df_combined.append(df_tempt)
    print(df_combined)

df_combined.to_csv("ticker.csv")