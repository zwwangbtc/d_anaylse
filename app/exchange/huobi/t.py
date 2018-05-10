#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def main(list):
    for i in list:
        # print("序号：%s   值：%s" % (list.index(i) + 1, i))
        # t = json.dumps(i)
        # print(i["currency"], i["type"], i["balance"])
        if i["currency"] == "usdt":
            if i["type"] == "trade":
                huobi_cny_usdt = i["balance"]
            elif i["type"] == "frozen":
                huobi_cny_usdt_frozen = i["balance"]
    print(huobi_cny_usdt,huobi_cny_usdt_frozen)


if __name__ == '__main__':
    obj = {"status": 'ok', 'data':
           {'id': 3540104, 'type': 'spot', 'state': 'working',
            'list': [
                {'currency': 'ht', 'type': 'trade',
                 'balance': '0.000000000000000000'},
                {'currency': 'ht', 'type': 'frozen',
                 'balance': '0.000000000000000000'},
                {'currency': 'usdt', 'type': 'trade',
                    'balance': '1.000000000000000000'},
                {'currency': 'usdt', 'type': 'frozen',
                    'balance': '0.000000000000000000'}
            ]}}

    # array = json.loads(obj["data"]["list"])
    # arr = json.dumps(obj["data"]["list"])

    list = obj["data"]["list"]
    # print(list)
    main(list)