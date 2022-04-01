from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list),
    path('<int:review_pk>/', views.review_details),
    path('product=<int:product_pk>/', views.product_reviews),
]