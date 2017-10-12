from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orders/producer/(?P<producer_pk>\d+)$', views.ListOrderItemsToProducer.as_view(), name='orders_items'),
    url(r'^baseproducts/$', views.ListCreateProductType.as_view(), name='base_products'),
    url(r'^baseproducts/(?P<pk>\d+)/$', views.RetriveUpdateDestroyProductType.as_view(), name='baseproducts_detail'),
    url(r'^user/$', views.register_consumer,name='register_consumer'),
    url(r'^login/$', views.login,name='register_consumer'),
    url(r'(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.consumer_details,name='consumer_details'),
    url(r'^lastorder/consumer/(?P<consumer_pk>\d+)$', views.RetrieveOrderByConsumer.as_view(),
        name='order_by_consumer'),

]