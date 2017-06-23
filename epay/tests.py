from django.test import TestCase


# Create your tests here.
from models import PaymentOrder

class DBTest(TestCase):

    def test(self):
        sql = 'SELECT PAYMENT_ORDER_ID as paymentOrderId, ORDER_ID as orderId, AMOUNT as amount, ORDER_TIME as orderTime, STATUS as status FROM T_PAYMENT_ORDER where payment_order_id=%s'
        poid='032016030103040201402550'
        orders = PaymentOrder.objects.raw(sql, [poid])
        for order in orders:
            print order.orderId

if __name__ == '__main__':
    DBTest.main()