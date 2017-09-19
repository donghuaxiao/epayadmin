# -*- coding:utf-8 -*-

from django import template
import json
import time
import logging

register = template.Library()

@register.filter('status')
def status(value):
    if value == 1:
        return u'有效'
    return u'停用'

def repay_status(value):
    val = str(value)
    if val == 1:
        return u'支持'
    return u'不支持'

@register.filter('to_time')
def to_time(value):
    logging.debug("value ", value)
    try:
        secs = long(value)
        exec_time = time.gmtime(secs / 1000)
        return time.strftime('%Y-%m-%d %H:%M:%S', exec_time)
    except Exception as ex:
        logging.exception(ex.message)
        return value

register.filter('repay_status', repay_status)