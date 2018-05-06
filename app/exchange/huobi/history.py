#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random

import pandas as pd

from utils.errors import *

valid_security_list = ["huobi_cny_btc", "huobi_cny_ltc"]

frequency_to_seconds = {
    "1m": 60,
    "5m": 5 * 60,
    "15m": 15 * 60,
    "30m": 30 * 60,
    "60m": 60 * 60,
    "1d": 60 * 60 * 24,
    "1w": 60 * 60 * 24 * 7,
    "1M": 60 * 60 * 24 * 30,
    "1y": 60 * 60 * 24 * 360
}


# TODO: 需要获取真实的历史数据，这里仅仅是一个Mock API
# TODO: 需要加入current bar time 的check
def get_current_price(security):
    # 取得最近1 minute bar的close
    minute_hist = get_price(security, count=1, frequency="1m")
    if len(minute_hist.index) < 1:
        raise ValueError("no valid 1 minute price")
    current_price = minute_hist['close'][-1]
    return current_price


# TODO: 需要获取真实的历史数据，这里仅仅是一个Mock API
# TODO: 需要加入current bar time 的check
def get_price(security, count=None, start_bar_time=None, end_bar_time=None, frequency="5m"):
    if count is not None and start_bar_time is not None:
        raise InvalidFilterError

    if security not in valid_security_list:
        raise InvalidSecurityError

    result = {"bar_time": [],
              "security": [],
              "open": [],
              "high": [],
              "low": [],
              "close": [],
              "volume": []}

    if security == "huobi_cny_btc":
        base_price = 4000
        base_volume = 10
        std_dev = 30
        deviation = 3
    else:
        base_price = 25
        base_volume = 100
        std_dev = 5
        deviation = 3

    if count is not None:
        # 取end_bar_time之前（不包括end_bar_time)count根bar
        if end_bar_time is None:
            end_bar_time = datetime.datetime.now()
        last_record_time_stamp = end_bar_time
        open = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
        close = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
        high = max(open, close) + random.uniform(1, 2)
        low = min(open, close) - random.uniform(1, 2)
        volume = base_volume + random.uniform(-3, 3)
        result["bar_time"].append(last_record_time_stamp)
        result["security"].append(security)
        result["open"].append(open)
        result["high"].append(high)
        result["low"].append(low)
        result["close"].append(close)
        result["volume"].append(volume)
        last_time = last_record_time_stamp

        i = count
        while i > 0:
            bar_time = last_time - datetime.timedelta(seconds=frequency_to_seconds[frequency])
            open = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
            close = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
            high = max(open, close) + random.uniform(1, 2)
            low = min(open, close) - random.uniform(1, 2)
            volume = base_volume + random.uniform(-3, 3)
            result["bar_time"].append(bar_time)
            result["security"].append(security)
            result["open"].append(open)
            result["high"].append(high)
            result["low"].append(low)
            result["close"].append(close)
            result["volume"].append(volume)
            last_time = bar_time
            i = i - 1

        result["bar_time"].reverse()
        result["security"].reverse()
        result["open"].reverse()
        result["high"].reverse()
        result["low"].reverse()
        result["close"].reverse()
        result["volume"].reverse()
        result = pd.DataFrame(result)
        result.index = result["bar_time"]
        return result
    else:
        bar_time = start_bar_time
        if end_bar_time is None:
            end_bar_time = datetime.datetime.now()
        while bar_time < end_bar_time:
            open = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
            close = base_price + random.uniform(-1 * std_dev * deviation, std_dev * deviation)
            high = max(open, close) + random.uniform(1, 2)
            low = min(open, close) - random.uniform(1, 2)
            volume = base_volume + random.uniform(-3, 3)
            result["bar_time"].append(bar_time)
            result["security"].append(security)
            result["open"].append(open)
            result["high"].append(high)
            result["low"].append(low)
            result["close"].append(close)
            result["volume"].append(volume)
            bar_time = bar_time + datetime.timedelta(seconds=frequency_to_seconds[frequency])
        result = pd.DataFrame(result)
        result.index = result["bar_time"]
        return result


def get_all_securities():
    result = {"security": [],
              "exchange": [],
              "settlement_currency": []}
    result["security"].append("huobi_cny_btc")
    result["exchange"].append("huobi")
    result["settlement_currency"].append("cny")

    result["security"].append("huobi_cny_ltc")
    result["exchange"].append("huobi")
    result["settlement_currency"].append("cny")
    result = pd.DataFrame(result)
    return result