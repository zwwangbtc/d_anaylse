# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 策略代码总共分为三大部分，1)PARAMS变量 2)intialize函数 3)handle_data函数
# 请根据指示阅读。或者直接点击运行回测按钮，进行测试，查看策略效果。

# 策略名称：Dual Thrust策略
# 关键词：追涨杀跌、价格通道、止损。
# 方法：
# 1)根据一段时间内的最高价，最低价和收盘价，计算出一个价格上下限；
# 2)当前价格突破上限时，全仓买入；当价格突破下线时，全仓卖出；
# 3)加入了止盈止损机制。

import numpy as np

# 阅读1，首次阅读可跳过:
# PARAMS用于设定程序参数，回测的起始时间、结束时间、滑点误差、初始资金和持仓。
# 可以仿照格式修改，基本都能运行。如果想了解详情请参考新手学堂的API文档。
PARAMS = {
    "start_time": "2015-01-01 00:00:00",  # 回测起始时间
    "end_time": "2016-10-10 00:00:00",  # 回测结束时间
    "slippage": 0.00001,  # 设置滑点
    "account_initial": {"huobi_cny_cash": 100000,
                        "huobi_cny_btc": 0},  # 设置账户初始状态
}


# 阅读2，遇到不明白的变量可以跳过，需要的时候回来查阅:
# initialize函数是两大核心函数之一（另一个是handle_data），用于初始化策略变量。
# 策略变量包含：必填变量，以及非必填（用户自己方便使用）的变量
def initialize(context):
    # 以日为单位进行回测
    context.frequency = "1d"
    # 设定以比特币为基准
    context.benchmark = "huobi_cny_btc"
    # 设定操作的标的为比特币
    context.security = "huobi_cny_btc"

    # 设置策略参数
    # 计算HH,HC,LC,LL所需的历史bar数目，用户自定义的变量，可以被handle_data使用;如果只需要看之前1根bar，则定义window_size=1
    context.user_data.window_size = 5
    # 用户自定义的变量，可以被handle_data使用，触发多头的range
    context.user_data.K1 = 0.2
    # 用户自定义的变量，可以被handle_data使用，触发空头的range.当K1<K2时，多头相对容易被触发,当K1>K2时，空头相对容易被触发
    context.user_data.K2 = 0.5
    # 止损线，用户自定义的变量，可以被handle_data使用
    context.user_data.portfolio_stop_loss = 0.75
    # 用户自定义变量，记录下是否已经触发止损
    context.user_data.stop_loss_triggered = False
    # 止盈线，用户自定义的变量，可以被handle_data使用
    context.user_data.portfolio_stop_win = 5.0
    # 用户自定义变量，记录下是否已经触发止盈
    context.user_data.stop_win_triggered = False


# 阅读3，策略核心逻辑：
# handle_data函数定义了策略的执行逻辑，按照frequency生成的bar依次读取并执行策略逻辑，直至程序结束。
# handle_data和bar的详细说明，请参考新手学堂的解释文档。
def handle_data(context):
    # 若已触发止盈/止损线，不会有任何操作
    if context.user_data.stop_loss_triggered:
        context.log.warn("已触发止损线, 此bar不会有任何指令 ... ")
        return
    if context.user_data.stop_win_triggered:
        context.log.info("已触发止盈线, 此bar不会有任何指令 ... ")
        return

    # 检查是否到达止损线或者止盈线
    if context.account.huobi_cny_net < context.user_data.portfolio_stop_loss * context.account_initial.huobi_cny_net or context.account.huobi_cny_net > context.user_data.portfolio_stop_win * context.account_initial.huobi_cny_net:
        should_stopped = True
    else:
        should_stopped = False

    # 如果有止盈/止损信号，则强制平仓，并结束所有操作
    if should_stopped:
        # 低于止损线，需要止损
        if context.account.huobi_cny_net < context.user_data.portfolio_stop_loss * context.account_initial.huobi_cny_net:
            context.log.warn(
                "当前净资产:%.2f 位于止损线下方 (%f), 初始资产:%.2f, 触发止损动作" %
                (context.account.huobi_cny_net, context.user_data.portfolio_stop_loss,
                 context.account_initial.huobi_cny_net))
            context.user_data.stop_loss_triggered = True
        # 高于止盈线，需要止盈
        else:
            context.log.warn(
                "当前净资产:%.2f 位于止盈线上方 (%f), 初始资产:%.2f, 触发止盈动作" %
                (context.account.huobi_cny_net, context.user_data.portfolio_stop_win,
                 context.account_initial.huobi_cny_net))
            context.user_data.stop_win_triggered = True

        if context.user_data.stop_loss_triggered:
            context.log.info("设置 stop_loss_triggered（已触发止损信号）为真")
        else:
            context.log.info("设置 stop_win_triggered （已触发止损信号）为真")

        # 需要止盈/止损，卖出全部持仓
        if getattr(context.account, context.security) > 0:
            # 卖出时，全仓清空
            context.log.info("正在卖出 %s" % context.security)
            context.order.sell(context.security, quantity=str(getattr(context.account, context.security)))
        return

    # 获取历史数据, 取后window_size+1根bar
    hist = context.data.get_price(context.security, count=context.user_data.window_size + 1,
                                  frequency=context.frequency)
    # 判断读取数量是否正确
    if len(hist.index) < (context.user_data.window_size + 1):
        context.log.warn("bar的数量不足, 等待下一根bar...")
        return

    # 取得最近1 根 bar的close价格
    latest_close_price = context.data.get_current_price(context.security)

    # 开始计算N日最高价的最高价HH，N日收盘价的最高价HC，N日收盘价的最低价LC，N日最低价的最低价LL
    hh = np.max(hist['high'].tail(context.user_data.window_size))
    hc = np.max(hist['close'].tail(context.user_data.window_size))
    lc = np.min(hist['close'].tail(context.user_data.window_size))
    ll = np.min(hist['low'].tail(context.user_data.window_size))
    price_range = max(hh - lc, hc - ll)

    # 取得倒数第二根bar的close, 并计算上下界限
    up_bound = hist['close'].iloc[-2] + context.user_data.K1 * price_range
    low_bound = hist['close'].iloc[-2] - context.user_data.K2 * price_range

    context.log.info('当前 价格：%s, 上轨：%s, 下轨: %s' % (latest_close_price, up_bound, low_bound))

    # 产生买入卖出信号，并执行操作
    if latest_close_price > up_bound:
        if context.account.huobi_cny_cash > 0:
            # 买入信号，且持有现金，则市价单全仓买入
            context.log.info("价格突破上轨，产生买入信号")
            context.log.info("正在买入 %s" % context.security)
            context.log.info("下单金额为 %s 元" % context.account.huobi_cny_cash)
            context.order.buy(context.security, cash_amount=str(context.account.huobi_cny_cash))
    elif latest_close_price < low_bound:
        if getattr(context.account, context.security) > 0:
            # 卖出信号，且持有仓位，则市价单全仓卖出
            context.log.info("价格突破下轨，产生卖出信号")
            context.log.info("正在卖出 %s" % context.security)
            context.log.info("卖出数量为 %s" % getattr(context.account, context.security))
            context.order.sell(context.security, quantity=str(getattr(context.account, context.security)))