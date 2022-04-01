# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from django.shortcuts import get_list_or_404
from .serializers import ReviewSerializer
from .models import Review
from rest_framework import generics

#   <<CLASS-BASED VIEWS W/ GENERIC VIEWS>>
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_pk']
        return get_list_or_404(Review, product=product_id)


#   <<CLASS-BASED VIEWS>>
#
# class ReviewList(APIView):
#     '''
#     List all reviews, or add a new review instance
#     '''
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ReviewDetail(APIView):
#     '''
#     Retrieve, update, or delete a review instance
#     '''
#     def get(self, request, review_pk):
#         review = get_object_or_404(Review, pk=review_pk)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

#     def put(self, request, review_pk):
#         review = get_object_or_404(Review, pk=review_pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, review_pk):
#         review = get_object_or_404(Review, pk=review_pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProductReviewList(APIView):
#     '''
#     List all reviews of a given product
#     '''
#     def get(self, request, product_pk):
#         reviews = get_list_or_404(Review,product=product_pk)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)


#   <<FUNCTION-BASED VIEWS>>
# @api_view(['GET', 'POST'])
# def reviews_list(request):

#     if request.method == 'GET':
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT','DELETE'])
# def review_details(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)

#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(review, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def product_reviews(request, product_pk):

#     if request.method == 'GET':
#         reviews = get_list_or_404(Review,product=product_pk)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)


