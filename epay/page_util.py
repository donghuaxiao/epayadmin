# -*- coding:utf-8 -*-

import logging
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

logger = logging.getLogger('epay.page_util')


def get_count_sql(query_sql):
    if query_sql is None:
        return None
    lower_query_sql = query_sql.lower()
    pos = lower_query_sql.index('from')
    return "select count(*) %s" % query_sql[pos:]


def get_pager_sql(query_sql, dialect):
    if dialect.lower() == 'oracle':
        return get_oracle_pager_sql(query_sql)
    return None


def get_oracle_pager_sql(query_sql):
    if query_sql is None:
        return None
    logger.debug('oralce paginator sql: %s ' % query_sql)
    sql_builder = StringIO()
    sql_builder.write("select * from( select t.*,rownum rn from( ")
    sql_builder.write(query_sql)
    sql_builder.write(" )t where rownum <= %s) where rn > %s")
    page_sql = sql_builder.getvalue()
    sql_builder.close()
    return page_sql


if __name__ == '__main__':
    sql = '''SELECT PAYMENT_ORDER_ID as paymentOrderId, ORDER_ID as orderId, AMOUNT as amount, 
            ORDER_TIME as orderTime STATUS as status
            FROM T_PAYMENT_ORDER where order_time between %s and %s'''
    page_sql = get_pager_sql(sql, 'oracle')

    count_sql = get_count_sql(sql)

    print page_sql % ('20170103000000', '20170105000000', 50, 20)
    print count_sql % ('20170103000000', '20170105000000')
