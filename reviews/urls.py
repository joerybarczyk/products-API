from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.product_reviews),
    path('reviews/<int:review_pk>/', views.review_details),
]