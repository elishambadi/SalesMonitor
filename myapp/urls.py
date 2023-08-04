from django.urls import path
from . import views

urlpatterns = [
    # Home URL
    path('', views.home, name='home'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),

    # Call views
    path('add_call/', views.add_call, name='add_call'),
    path('view_calls/', views.view_calls, name='view_calls'),
    path('delete_call/<int:pk>/', views.delete_call, name='delete_call'),
    path('call_detail/<int:pk>/', views.call_detail, name='call_detail'),

    # Channel views
    path('add_channel/', views.add_channel, name='add_channel'),
    path('view_channels/', views.view_channels, name='view_channels'),
    path('delete_channel/<int:pk>/', views.delete_channel, name='delete_channel'),
    path('channel_detail/<int:pk>/', views.channel_detail, name='channel_detail'),

    # Representative views
    path('add_representative/', views.add_representative, name='add_representative'),
    path('view_representatives/', views.view_representatives, name='view_representatives'),
    path('delete_representative/<int:pk>/', views.delete_representative, name='delete_representative'),
    path('representative_detail/<int:pk>/', views.representative_detail, name='representative_detail'),

    # Payment views
    path('add_payment/', views.add_payment, name='add_payment'),
    path('view_payments/', views.view_payments, name='view_payments'),
    path('delete_payment/<int:pk>/', views.delete_payment, name='delete_payment'),
    path('payment_detail/<int:pk>/', views.payment_detail, name='payment_detail'),

    # Sale views
    path('add_sale/', views.add_sale, name='add_sale'),
    path('view_sales/', views.view_sales, name='view_sales'),
    path('delete_sale/<int:pk>/', views.delete_sale, name='delete_sale'),
    path('sale_detail/<int:pk>/', views.sale_detail, name='sale_detail'),
]
