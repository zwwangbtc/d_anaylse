#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""define bitvc errors"""


# pylint: disable=C0301

def error_text(error_num):
    """figure out our errors"""
    try:
        return ERRORS[error_num]
    except KeyError:
        return "Undefined Error"


# used some vim-fu to help format this
ERRORS = {
    10000: "必选参数不能为空",
    10001: "用户请求过于频繁",
    10002: "系统错误",
    10003: "未在请求限制列表中,稍后请重试",
    10004: "IP限制不能请求该资源",
    10005: "密钥不存在 ",
    10006: "用户不存在",
    10007: "签名不匹配",
    10008: "非法参数",
    10009: "订单不存在",
    10010: "余额不足",
    10011: "买卖的数量小于BTC/LTC最小买卖额度",
    10012: "当前网站暂时只支持btc_cny ltc_cny",
    10013: "此接口只支持https请求",
    10014: "下单价格不得≤0或≥1000000",
    10015: "下单价格与最新成交价偏差过大",
}