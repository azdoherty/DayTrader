import numpy as np
import pandas as pd
import requests
from datetime import datetime, timedelta
import config
import json
from flask import jsonify
from matplotlib import pyplot as plt
import io
import base64


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
    result_df = build_dataframe(res.json(), start, stop)
    return result_df


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
    print(jsonResponse)
    dataDict = jsonResponse["Time Series (Daily)"]
    for dtp in dataDict:
        dtime = pd.to_datetime(dtp, format="%Y-%m-%d")
        if dtime in df.index:
            for key, value in dataDict[dtp].items():
                df.loc[dtime.date(), key.split()[-1]] = float(value)
    return df


class Asset:
    def __init__(self, symbol, start=None, stop=None):
        self.symbol = symbol
        self.asset_data = get_daily_stock_data(symbol, start, stop)
        self.clean_data()

    def clean_data(self):
        self.asset_data = self. asset_data.fillna(method='ffill')

    def plot_image(self):
        img = io.BytesIO()
        ax = plt.figure()
        self.asset_data['close'].plot()
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.title(f"Price for {self.symbol}")
        plt.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        url = 'data:image/png;base64,{}'.format(graph_url)
        print(f"URL: {url}")
        return url

if __name__ == "__main__":
    start = pd.to_datetime("2018-01-02", format="%Y-%m-%d")
    stop = pd.to_datetime("2019-02-18", format="%Y-%m-%d")
    asset = Asset("MSFT", start, stop)
    asset.plot_image()

