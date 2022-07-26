from django.urls import path
from delivery import views

urlpatterns = [
    path('orders/', views.order_list, name="order_list"),
    # path('timeinput/', views.timeinput, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('order/',views.order, name='order')
    
]