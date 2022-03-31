from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer
from .models import Review

@api_view(['GET'])
def product_reviews(request, product_pk):
    reviews = get_list_or_404(Review,product=product_pk)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
