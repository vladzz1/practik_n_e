from django.urls import path
from . import views

app_name='products'

urlpatterns = [
    path('', views.show_products, name='show_products'),
    path('create/', views.products_create, name='create')
]