from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('<int:review_pk>/', views.ReviewDetail.as_view()),
    path('product/<int:product_pk>/', views.ProductReviewList.as_view()),
]