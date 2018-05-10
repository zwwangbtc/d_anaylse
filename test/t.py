import requests
from bs4 import BeautifulSoup as bs
import urllib3
import sys

import sys
sys.path.append("../")

from config import accountConfig

# 初始化SERVICE_PRICE
SERVICE_API = accountConfig.SERVICE_PRICE["USD"]["SERVICE_API"]


def getPrice(symbol):
    s = requests.get(SERVICE_API).text
    soup = bs(s, "html.parser")
    tag = soup.findAll("td", attrs={"class": {"ticker", "lastprice"}})
    # print(tag)
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
        if tmp == symbol:
            f = 0
            continue
    # print(tmp)
    return tmp.replace("$ ", "")


def testSoup():
    str = "<html> <head> <title>Page title</title></head><body><p id=\"firstpara\" align=\"center\">This is paragraph<b>one</b>.</p><p id=\"secondpara\" align=\"blah\">This is paragraph<b>two</b>.</p></body></html>"
    soup = bs(str, "html.parser")
    tt = soup.find("body")
    # tt = soup.find(['head', 'body'])
    # tt = soup.find(attrs={'id':re.compile('xxx'), 'algin':'xxx')
    print(tt)


if __name__ == '__main__':
    # BTC/ETH/ETC/LTC/BCH/USDT
    symbol = "BTC"
    print(getPrice(symbol))
    # testSoup()