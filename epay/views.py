# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
import db_utils
import page_util
import logging
import time
import json
import datetime_util
from models import MerchantChannelServiceModel, CronJob
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from dao import dbcache
from paginator import RawQuerySetPaginator as RawPaginator

# Create your views here.

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

LOG = logging.getLogger(__name__)


def get_len(rawqueryset):
    def __len__(self):
        params = ["""'%s'""" % p for p in self.params]
        count_sql = page_util.get_count_sql(rawqueryset.raw_query)
        print "count sql: %s" % count_sql
        with connection.cursor() as cursor:
            cursor.execute(count_sql % tuple(params))
            row = cursor.fetchone()
            return row[0]
    return __len__


def order_list(request):
    sql = '''SELECT PAYMENT_ORDER_ID as paymentOrderId, ORDER_ID as orderId, AMOUNT as amount, 
        ORDER_TIME as orderTime, STATUS as status FROM T_PAYMENT_ORDER
        WHERE (status = 2 or status = 3)'''
    sql_buf = StringIO()
    sql_buf.write(sql)

    if request.method == 'GET':
        return render(request, 'order/orderlist.html')
    query_params = []
    paymentOrderId = request.POST.get('paymentOrderId')

    orderId = request.POST.get('orderId')
    endtime = request.POST.get('endtime')
    if endtime:
        end_time = datetime_util.convert_datetime_to_str(endtime)

    starttime = request.POST.get('starttime')
    if starttime:
        start_time = datetime_util.convert_datetime_to_str(starttime)
    print request.POST
    print "paymentOrderId = %s" % paymentOrderId
    print "orderId = %s " % orderId

    if paymentOrderId:
        sql_buf.write(" AND payment_order_id = %s")
        query_params.append(paymentOrderId)
    elif orderId:
        sql_buf.write(" AND order_id = %s")
        query_params.append(orderId)
    else:
        sql_buf.write(" AND create_time between %s and %s")
    print "query sql: %s" % sql

    orders = []
    before_time = time.time()
    print "before query: %s" % before_time
    start_time = '20170301000000'
    end_time = '20170305230000'
    page_params = {'page': 2, 'pageSize': 20}

    pageObj = db_utils.query_for_list_page(sql_buf.getvalue(), [start_time, end_time], page_params, 'oracle')

    return render(request, 'order/orderlist.html', {'pageObj': pageObj, 'nav': u'订单'})


def index(request):
    return render(request, 'base.html')


def get_channel(request):
    channel_list = [{'id': item.channelId, 'name': item.channelName} for item in dbcache.get_cache('channels')]
    return JsonResponse(json.dumps(channel_list, ensure_ascii=False), safe=False)


def get_serivces(request):
    services_list = [{'id': item.service_id, 'name': item.title} for item in dbcache.get_cache('services')]
    return JsonResponse(json.dumps(services_list, ensure_ascii=False), safe=False)


def get_merchant(request):
    merchants = [{'id': item.user_id, 'name': item.title} for item in dbcache.get_cache('merchants') if item.status != 0]
    return JsonResponse(json.dumps(merchants, ensure_ascii=False), safe=False)


def list_channels(request):

    channels = dbcache.get_cache('channels')
    page = int(request.GET.get('page', '1'))
    paginator = Paginator(channels, 10)

    try:
        channels = paginator.page(page)
        print channels
    except PageNotAnInteger:
        channels = paginator.page(1)
    except EmptyPage:
        channels = paginator(paginator.num_pages)
    return render(request, 'channel/channel.html', {'channels': channels, 'nav': u'渠道'})


def list_payment_org(request):
    page = int(request.GET.get('page', '1'))
    payment_orgs = dbcache.get_cache('payorgs')
    p = Paginator(payment_orgs, 10)
    try:
        payment_orgs = p.page(page)
    except PageNotAnInteger as ex:
        payment_orgs = p.page(1)
    return render(request, 'paymentorg/org.html', {'orgs': payment_orgs})


def list_merchant_channel_service(request):
    query_sql = StringIO()
    query_sql.write("SELECT 1 as id, tpu.USER_ID as merchant_id, tpu.TITLE as merchant_name, tc.CHANNEL_ID,")
    query_sql.write(" tc.TITLE AS CHANNEL_NAME, tps.SERVICE_ID, tps.TITLE as SERVICE_NAME, tpa.ACCOUNT_ID, tpo.ORG_ID,tpo.ORG_NAME ")
    query_sql.write(" FROM T_PAYMENT_USER tpu, T_CHANNEL tc,T_CHANNEL_MERCHANT tcm, T_PAYMENT_SERVICE tps, ")
    query_sql.write(" T_CHANNEL_SERVICE tcs, T_PAYMENT_ACCOUNT tpa, T_PAYMENT_DELEGATION tpd, T_PAYMENT_ORG tpo ")
    query_sql.write(" WHERE tc.CHANNEL_ID = tcm.CHANNEL_ID AND tpu.USER_ID = tcm.USER_ID")
    query_sql.write(" AND tc.CHANNEL_ID = tcs.CHANNEL_ID AND tps.SERVICE_ID = tcs.SERVICE_ID")
    query_sql.write(" AND tps.SERVICE_ID= tpd.SERVICE_ID AND tpd.ACCOUNT_ID = tpa.ACCOUNT_ID AND tpu.USER_ID = tpa.USER_ID")
    query_sql.write(" AND tpd.ORG_ID = tpo.ORG_ID and tpa.ORG_ID = tpo.ORG_ID")

    params = []
    channel_id = request.POST.get('channel_id')
    service_id = request.POST.get('service_id')
    merchant_id = request.POST.get('merchant_id')

    if channel_id is not None and channel_id != u'':
        query_sql.write(" AND tc.CHANNEL_ID = %s")
        params.append(channel_id)
    if service_id is not None and service_id != u'':
        query_sql.write(" AND tps.SERVICE_ID = %s")
        params.append(service_id)
    if merchant_id is not None and merchant_id != u'':
        query_sql.write(" AND tpu.USER_ID = %s")
        params.append(merchant_id)

    sql = query_sql.getvalue()
    query_sql.close()

    qs = MerchantChannelServiceModel.objects.raw(sql, params if len(params) > 0 else None)
    page_num = request.POST.get('page')
    if page_num is None or page_num == u'':
        page_num = 1
    else:
        page_num = int(page_num)
    try:
        p = RawPaginator(qs, 10)
        results = p.page(page_num)
    except Exception as e:
        print e.message
        results = p.page(1)

    return render(request, 'merchant_channel_service_payorg.html', {'results': results, 'title': u'商户渠道业务支付方式'})


def job(request):
    sql_builder = StringIO()
    sql_builder.write('SELECT 1 as ID, tr.TRIGGER_NAME, tr.JOB_NAME, qct.CRON_EXPRESSION, tr.NEXT_FIRE_TIME, tr.PREV_FIRE_TIME, tr.TRIGGER_STATE')
    sql_builder.write(' FROM QRTZ_TRIGGERS tr, QRTZ_CRON_TRIGGERS qct')
    sql_builder.write(' WHERE tr.TRIGGER_NAME = qct.TRIGGER_NAME')

    sql = sql_builder.getvalue()
    sql_builder.close()

    qs = CronJob.objects.raw(sql)
    setattr(type(qs), '__len__', get_len(qs))
    page_num = request.POST.get('page')
    if page_num is None or page_num == u'':
        page_num = 1
    else:
        page_num = int(page_num)
    try:
        p = RawPaginator(qs, 10)
        jobs = p.page(page_num)
        print jobs
    except Exception as e:
        print e.message
        jobs = p.page(1)

    return render(request, 'jobs.html', {'jobs': jobs, 'title': u'定时任务'})