from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list),
    path('<int:pk>/', views.product_details)
]