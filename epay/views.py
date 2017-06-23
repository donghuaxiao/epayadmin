from django.shortcuts import render
from django.db import connection
from models import PaymentOrder
# Create your views here.

def order_list(request):
    sql = 'SELECT PAYMENT_ORDER_ID as paymentOrderId, ORDER_ID as orderId, AMOUNT as amount, ORDER_TIME as orderTime, STATUS as status FROM T_PAYMENT_ORDER where payment_order_id=%s'
    poid = '032016030103040201402550'
    orders = []
    with connection.cursor() as cursor:
        cursor.execute(sql, [poid])
        results = cursor.fetchall()
        desc = cursor.description
        orders = [ dict(zip([col[0].lower() for col in desc], row)) for row in results]
    #orders = PaymentOrder.objects.raw(sql, [poid])

    return render(request, 'order/orderlist.html', {'orders': orders, 'nav': 'Order'})

def index(request):
    return render(request, 'base2.html')