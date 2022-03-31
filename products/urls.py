from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.products_list),
    path('<int:product_pk>/', views.product_details),
    
]