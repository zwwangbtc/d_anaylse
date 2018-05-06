#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httpMD5Util import httpGet, httpPost

def ticker(url,symbol=''):
    TICKER_RESOURCE = "api/getTicker"
    params = ''
    if symbol:
        params = 'symbol=%(symbol)s' % {'symbol': symbol}
    return httpGet(url, TICKER_RESOURCE, params)
