from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyView.as_view(), name = ''),
    path('order/<id>', views.OrderView.as_view(), name='order_url')
]
