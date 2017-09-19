# -*- coding:utf-8 -*-

from datetime import datetime
import logging
import exceptions
LOG = logging.getLogger(__file__)
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
STR_TIME_FORMAT ='%Y%m%d%H%M%S'

def convert_datetime_to_str(s_time, from_format=TIME_FORMAT, to_format=STR_TIME_FORMAT):
    try:
        dt = datetime.strptime(s_time, from_format)
        return dt.strftime(to_format)
    except ValueError as e:
        LOG.error(e.message)
        raise exceptions.DateTimeFormatException(e.message)
