from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'orders$', views.order_list, name='orderlist'),
    url(r'index$', views.index, name='index'),
    url(r'ajax_channels$', views.get_channel, name='channels'),
    url(r'channels$', views.list_channels, name='listchannels'),
    url(r'orgs', views.list_payment_org, name='list_orgs'),
    url(r'cmsp', views.list_merchant_channel_service, name='list_merchant_channel_service'),
    url(r'ajax_services$', views.get_serivces, name='services'),
    url(r'ajax_merchants$', views.get_merchant, name='merchants'),
    url(r'jobs$', views.job, name='jobs'),
]