import numpy as np
import pandas as pd
import requests
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
    result_df = build_dataframe(res.json, start, stop)


def build_dataframe(jsonResponse, start, stop):
    df = pd.DataFrame()



if __name__ == "__main__":
    start = pd.to_datetime("2018-01-01", format="%Y-%m-%d")
    stop = pd.to_datetime("2019-01-01", format="%Y-%m-%d")
    get_daily_stock_data("MSFT", start=start, stop=stop)

