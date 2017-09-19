# -*- coding:utf-8 -*-
from django.db import connection
import page_util
import exceptions


def query_object(query_sql, params):
    with connection.cursor() as cursor:
        cursor.execute(query_sql, params)
        result = cursor.fetchone()
        return result[0]


def query_for_list(query_sql, params):
    with connection.cursor() as cursor:
        cursor.execute(query_sql, params)
        results = cursor.fetchall()
        desc = cursor.description
        list_result = [dict(zip([col[0].lower() for col in desc], row)) for row in results]
        return list_result


def query_for_list_page(query_sql, params, page_params, dialect):
    if query_sql is None:
        raise exceptions.SQLException("sql is None")
    count_sql = page_util.get_count_sql(query_sql)
    count = query_object(count_sql, params)
    if count == 0:
        return {'count': 0, 'list': [], 'page': 0, 'pageSize': 0, 'totalPage': 0}
    query_pager_sql = page_util.get_pager_sql(query_sql, 'oracle')
    page_size = 0 if page_params.get('pageSize') is None else int(page_params.get('pageSize'))
    page = 0 if page_params.get('page') else int(page_params.get('page'))
    start_page = (page_params.get('page')-1) * page_size
    end_page = start_page + page_size
    params.append(end_page)
    params.append(start_page)
    results = query_for_list(query_pager_sql, params)
    return {'count': count,
            'list': results,
            'page': page,
            'pageSize': page_size,
            'totalPage': (count + 1) / page_size}
