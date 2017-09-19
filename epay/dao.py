# -*- coding:utf-8 -*-

from models import Channel, TPaymentUser, TPaymentService, PaymentOrg


class DBCache(object):
    cache = {}

    def __init__(self):
        self.load_channels()
        self.load_merchants()
        self.load_services()
        self.load_pay_org()

    def load_channels(self):
        channels = Channel.objects.all()
        self.cache['channels'] = list(channels)

    def load_merchants(self):
        merchants = TPaymentUser.objects.filter(user_type__gte=2)
        self.cache['merchants'] = list(merchants)

    def load_services(self):
        services = TPaymentService.objects.all()
        self.cache['services'] = list(services)

    def load_pay_org(self):
        payorgs = PaymentOrg.objects.all()
        self.cache['payorgs'] = list(payorgs)

    def get_cache(self, name):
        return self.cache.get(name, None)

dbcache = DBCache()