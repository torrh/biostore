from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^offersproducer/(?P<producer_pk>\d+)$', views.ListOffersByProducer.as_view(), name='orders_by_producer'),
    url(r'^prueba/$', views.prueba, name="prueba "),
    url(r'^allproducts/$', views.all, name="todos los productos"),
#PRODUCTORES
    url(r'^addproduceroffer/$', views.create_offer_producer, name ="Crear oferta productor"),
    url(r'^producersoffers/$', views.ListProducerOffers.as_view(), name="Dar todas las ofertas"),
    url(r'^getproducerbyid/(?P<id>\d+)/$',views.getproducerbyid, name="Dar productor por id"),
    url(r'^ordersbyproducer/(?P<producer_pk>\d+)/$', views.ListOrderItemsToProducer.as_view(), name='orders_items'),
    url(r'^updatepartialorder/(?P<pk>\d+)/$', views.updatePartialOrder.as_view(), name='update state order'),
    url(r'^updatestateorder/$',views.update_state_orders, name="Actualizar estado ordenes"),

#CONSUMER
    url(r'^createorder/$', views.create_order, name='create_order'),
    url(r'^orders/$', views.ListOrderItems.as_view(), name='list_orders'),
    url(r'^producers/$', views.give_all_producers, name='get all producers'),
#ADMINSTRADOR
    url(r'^updatepaymentorder/$', views.update_payment_orders, name="actualizar pagos administrador"),
    url(r'^editadminoffer/', views.edit_adminoffer, name="Editar oferta admin"),
    url(r'^addproducer/', views.register_producer, name="Registrar productor"),
    url(r'^productproducers/(?P<id>\d+)/$',views.producersdetailbyname, name="Dar productores de un producto por id"),
    url(r'^offersbyproducer/(?P<id>\d+)/$',views.getoffersbyproductorbyid, name="Ofertas de un productor"),
    url(r'^acceptedoffers/$',views.getacceptedproduceroffers, name="Dar ofertas aceptadas productores"),
    url(r'^saveoffers/$',views.save_producer_offers, name="Guardar ofertas productores"),
    url(r'^addadminoffer/$', views.create_offer_admin, name="Crear oferta administrador"),
    url(r'^adminoffers/$', views.ListAdminOffersItems.as_view(), name="Dar todas las ofertas administrador"),
    url(r'^baseproducts/$', views.ListCreateProductType.as_view(), name='base_products'),
    #NOTIFICATIONS
    url(r'^addnotification/$', views.add_notification, name='add notification'),
  #  url(r'^notifications/$', views.get_notification, name='get notification'),
    url(r'^baseproducts/(?P<pk>\d+)/$', views.RetriveUpdateDestroyProductType.as_view(), name='baseproducts_detail'),
    url(r'^user/$', views.register_consumer,name='register_consumer'),
    url(r'^login/$', views.login,name='login_consumer'),
    url(r'(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.consumer_details,name='consumer_details'),
    url(r'^lastorder/consumer/(?P<consumer_pk>\d+)$', views.RetrieveOrderByConsumer.as_view(),
        name='order_by_consumer'),
    url(r'^cancelorderitem/(?P<pk>\d+)/$', views.cancelOrderItem.as_view(), name='Cancel order item'),



]