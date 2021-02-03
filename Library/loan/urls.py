from django.urls import path
from .views import order, order_status

urlpatterns = [
    path('order-book/<id>', order, name='order-book'),
    path('order-status', order_status, name='order-status'),
]
