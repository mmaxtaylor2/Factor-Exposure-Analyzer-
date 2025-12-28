# factor_data.py

import pandas as pd
import yfinance as yf
from pandas_datareader.famafrench import FamaFrenchReader

# ----------------------------- #
# PRICE RETURNS
# ----------------------------- #
def get_price_data(ticker="SPY", start="2015-01-01"):
    data = yf.download(ticker, start=start)
    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]
    returns = close.pct_change().dropna()
    return returns.rename("Asset_Returns").to_frame()

# ----------------------------- #
# FACTOR RETURNS (Fama-French 3)
# ----------------------------- #
def get_factor_data(start="2015-01-01"):
    ff = FamaFrenchReader("F-F_Research_Data_Factors_daily", start=start)
    df = ff.read()[0] / 100.0       # convert % to decimals
    df = df.rename(columns={"Mkt-RF": "MKT"})
    df.index = pd.to_datetime(df.index)
    return df[["MKT", "SMB", "HML", "RF"]].dropna()

# ----------------------------- #
# MERGE DATASETS + EXCESS RETURN
# ----------------------------- #
def merge_data(ticker="SPY"):
    prices = get_price_data(ticker)
    factors = get_factor_data()
    df = prices.join(factors, how="inner")
    df["Excess_Return"] = df["Asset_Returns"] - df["RF"]
    return df

# ----------------------------- #
# TEST
# ----------------------------- #
if __name__ == "__main__":
    print(merge_data("SPY").head())

