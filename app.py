#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################
#   量化
#   策略
#   交易
###############################################################

from app.interExchangeSpread.interExchangeSpreadStrategy import *
from app.interExchangeSpread.fixedSpreadArbStrategy import *
from app.interExchangeSpread.statArbStrategy import *
from utils.helper import *

if __name__ == "__main__":
    # 传统搬砖 - BTC
    '''
    strat =interExchangeSpreadStrategy(datetime.datetime.now(), 
                            0.8, 
                            1, 
                            0.1, 
                            60, 
                            helper.COIN_TYPE_BTC_CNY)
    '''

    # 传统搬砖 - LTC, 加每日退出时间
    '''
    strat =interExchangeSpreadStrategy(datetime.datetime.now(), 
                            0.8, 
                            1, 
                            0.1, 
                            60, 
                            helper.COIN_TYPE_BTC_CNY,
                            dailyExitTime="23:30:00")
    '''

    # 统计套利搬砖 - BTC, 加每日退出时间, 加自动再平衡，加退出时自动再平衡
    '''
    strat = StatArbSignalGenerator(datetime.datetime.now(), 
                                   0.8, 
                                   1, 
                                   0.1, 
                                   60, 
                                   helper.COIN_TYPE_BTC_CNY,
                                   maximum_qty_multiplier=3,
                                   auto_rebalance_on=True,
                                   auto_rebalance_on_exit=True,
                                   dailyExitTime="23:30:00")
    '''

    # 统计套利搬砖 - LTC
    '''
    strat = StatArbSignalGenerator(datetime.datetime.now(), 
                                   0.8, 
                                   1, 
                                   0.1, 
                                   60, 
                                   helper.COIN_TYPE_BTC_CNY,
                                   maximum_qty_multiplier=3,
                                   auto_rebalance_on=False,
                                   auto_rebalance_on_exit=False)
    '''

    # 固定价差套利搬砖 - BTC
    strat = FixedSpreadSignalGenerator(datetime.datetime.now(),
                                       0.8,
                                       1,
                                       0.1,
                                       60,
                                       helper.COIN_TYPE_BTC_CNY,
                                       0.001,
                                       0.0005,
                                       maximum_qty_multiplier=3,
                                       auto_rebalance_on=False,
                                       auto_rebalance_on_exit=False)

    # 固定价差套利搬砖 - LTC, 加每日退出时间，加自动再平衡，加退出时自动再平衡
    '''
    strat = FixedSpreadSignalGenerator(datetime.datetime.now(),
                                       0.8, 
                                       1, 
                                       0.1, 
                                       60, 
                                       helper.COIN_TYPE_LTC_CNY,
                                       0.003,
                                       0.001,
                                       maximum_qty_multiplier=3,
                                       auto_rebalance_on=True,
                                       auto_rebalance_on_exit=True)
    '''
    start_strat(strat)
