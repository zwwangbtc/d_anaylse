#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 15:29:19
# @Author  : Ryan (tech@huobi.com)
# @Link    : https://www.huobi.com
# @Version : $Id$

from util import *
import app.exchange.huobi.huobiService as HuobiService

if __name__ == '__main__':
    # print("获取1分钟线")
    # print(HuobiService.get_kline('ethcny', '1min'))
    # print("获取合并深度为1的盘口")
    # print(HuobiService.get_depth('ethcny', 'step1'))
    # print("获取Trade Detail")
    # print(HuobiService.get_trade('ethcny'))
    # print("获取 Market Detail 24小时成交量数据")
    # print(HuobiService.get_detail('ethcny'))
    print("获取当前账户资产")
    print(HuobiService.getBalance())
    # print('下单')
    # print(HuobiService.orders(1, 'api', 'ethcny', 'buy-limit', 12))
    # print('执行订单')
    # print(HuobiService.place_order('58840'))
    # print('撤销订单')
    # print(HuobiService.cancel_order('58840'))
    # print('查询某个订单')
    # print(HuobiService.order_info('58840'))
    # print('查询某个订单的成交明细')
    # print(HuobiService.order_matchresults('45421'))
    # print('查询当前委托、历史委托')
    # print(HuobiService.orders_list('ethcny', 'submitted'))
    # print('查询当前成交、历史成交')
    # print(HuobiService.orders_matchresults('ethcny'))
    # print('查询虚拟币提币地址')
    # print(HuobiService.get_withdraw_address('eth'))