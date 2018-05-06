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
    'bad-request'                                 : "错误请求",
    'invalid-parameter'                           : "参数错",
    'invalid-command'                             : "指令错",
    'base-symbol-error'                           : "交易对不存在",
    'base-currency-error'                         : "币种不存在",
    'base-date-error'                             : "错误的日期格式 ",
    'account-transfer-balance-insufficient-error' : "余额不足无法冻结",
    'bad-argument'                                : "无效参数",
    'api-signature-not-valid'                     : "API签名错误",
    'gateway-internal-error'                      : "系统繁忙，请稍后再试",
    'security-require-assets-password'            : "需要输入资金密码",
    'audit-failed'                                : "下单失败",
    'ad-ethereum-addresss'                        : "请输入有效的以太坊地址",
    'order-accountbalance-error'                  : "账户余额不足",
    'order-limitorder-price-error'                : "限价单下单价格超出限制",
    'order-limitorder-amount-error'               : "限价单下单数量超出限制",
    'order-orderprice-precision-error'            : "下单价格超出精度限制",
    'order-orderamount-precision-error'           : "下单数量超过精度限制",
    'order-marketorder-amount-error'              : "下单数量超出限制",
    'order-queryorder-invalid'                    : "查询不到此条订单",
    'order-orderstate-error'                      : "订单状态错误",
    'order-datelimit-error'                       : "查询超出时间限制",
    'order-update-error'                          : "订单更新出错",
}
