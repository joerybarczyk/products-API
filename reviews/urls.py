from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_reviews),
    path('<int:review_pk>', views.review_details),
]