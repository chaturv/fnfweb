from django.conf.urls import url

from . import views


app_name = 'operations'

urlpatterns = [
    # /operations/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^delete/orders/$', views.DeleteOrderView.as_view(), name='delete-order'),
    url(r'^create/order/$', views.CreateOrderView.as_view(), name='create-order'),
    url(r'^generate/shopping-list/$', views.GenerateShoppingListView.as_view(), name='shopping-list'),
    url(r'^complete/order/$', views.CompleteOrderView.as_view(), name='complete-order'),
]