#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import urllib3
import sys

from config import accountConfig
# 初始化SERVICE_PRICE
SERVICE_API = accountConfig.SERVICE_PRICE["USD"]["SERVICE_API"]

class Account(object):
    # def __init__(self):
        
    def getPrice(self,currency):
        s = requests.get(SERVICE_API).text
        soup = bs(s, "html.parser")
        tag = soup.findAll("td", attrs={"class": {"ticker", "lastprice"}})
        f = 1
        t = 0
        for i in tag:
            tmp = i.getText().strip()
            t = t.__add__(1)
            # print(len(tag), t)
            if f == 0:
                break
            elif f == 1 and t == len(tag):
                tmp = "None"
                break
            if tmp == currency:
                f = 0
                continue
    # print(tmp)
        return tmp.replace("$ ", "")