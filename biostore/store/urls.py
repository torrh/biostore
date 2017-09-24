from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListCreateProduct.as_view(), name='product_list'),
    url(r'(?P<pk>\d+)/$', views.RetriveUpdateDestroyProduct.as_view(), name='product_detail'),
    url(r'^category/$', views.ListCreateCategory.as_view(), name='category'),
    url(r'^category/(?P<pk>\d+)/$', views.RetriveUpdateDestroyCategory.as_view(), name='category_detail'),
    url(r'^baseproducts/$', views.ListCreateProductType.as_view(), name='base_products'),
    url(r'^baseproducts/(?P<pk>\d+)/$', views.RetriveUpdateDestroyProductType.as_view(), name='baseproducts_detail')
]