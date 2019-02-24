import numpy as np
import pandas as pd
import requests
from datetime import datetime, timedelta
import config
import json
from flask import jsonify


def get_daily_stock_data(symbol, start=None, stop=None):
    """
    get stock data and return it as a pandas dataframe
    :param symbol: stock symbol
    :param start: start date
    :param stop: end date
    :return: dataframe of daily stock data
    """
    url = "https://www.alphavantage.co/query?"
    params = {
        "function":"TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": config.ALPHAVANTAGE_API_KEY,
    }
    res = requests.get(url, params=params)
    print(res.json())
    result_df = build_dataframe(res.json(), start, stop)


def build_dataframe(jsonResponse, start, stop):
    """
    build a dataframe of high/open/low/close
    :param jsonResponse: the reponse object from an alphavantage request
    :param start: date to start sequence, datetime object in Y-m-d format
    :param stop: date, date to end sequence
    :return:
    """
    days = pd.date_range(start, stop)

    df = pd.DataFrame({"days": days,
                       "open": None,
                       "high": None,
                       "low": None,
                       "close": None,
                       "volume": None})
    df = df.set_index("days")
    print(df)
    dataDict = jsonResponse["Time Series (Daily)"]
    for dtp in dataDict:
        dtime = pd.to_datetime(dtp, format="%Y-%m-%d")
        if dtime in df.index:
            for key, value in dataDict[dtp].items():
                df.loc[dtime.date(), key.split()[-1]] = float(value)

    print(df)




if __name__ == "__main__":
    start = pd.to_datetime("2018-01-02", format="%Y-%m-%d")
    stop = pd.to_datetime("2019-02-18", format="%Y-%m-%d")
    get_daily_stock_data("MSFT", start=start, stop=stop)

