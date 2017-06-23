from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'orders$', views.order_list, name='orderlist'),
    url(r'index$', views.index, name='index')
]