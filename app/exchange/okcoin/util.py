#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("../../../")

from  config import accountConfig
from app.exchange.okcoin.okcoinFutureAPI import OKCoinFuture
from app.exchange.okcoin.okcoinSpotAPI import OKCoinSpot

# 初始化ACCESS_KEY, SECRET_KEY, SERVICE_API
ACCESS_KEY = accountConfig.OKCOIN["USD_1"]["ACCESS_KEY"]
SECRET_KEY = accountConfig.OKCOIN["USD_1"]["SECRET_KEY"]
SERVICE_API = accountConfig.OKCOIN["USD_1"]["SERVICE_API"]



# 现货API
def getOkcoinSpot():
    return OKCoinSpot(SERVICE_API, ACCESS_KEY, SECRET_KEY)


# 期货API
def getOkcoinFuture():
    return OKCoinFuture(SERVICE_API, ACCESS_KEY, SECRET_KEY)
