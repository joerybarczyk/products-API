# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import status
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

#   <<CLASS-BASED VIEWS W/ GENERIC VIEWS>>
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



#   <<CLASS-BASED VIEWS W/ MIXINS>>
#
# class ProductList(mixins.ListModelMixin,
#                     mixins.CreateModelMixin,
#                     generics.GenericAPIView):
#     '''
#     List all products, or add a new product instance
#     '''

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

# class ProductDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     '''
#     Retrieve, update, or delete a product instance
#     '''

#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.delete(request, pk)



#   <<CLASS-BASED VIEWS>>
#
# class ProductList(APIView):
#     '''
#     List all products, or add a new product instance
#     '''
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ProductDetail(APIView):
#     '''
#     Retrieve, update, or delete a product instance
#     '''
#     def get(self, request, product_pk):
#         product = get_object_or_404(Product, pk=product_pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, product_pk):
#         product = get_object_or_404(Product, pk=product_pk)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, product_pk):
#         product = get_object_or_404(Product, pk=product_pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#   <<FUNCTION-BASED VIEWS>>
#
# @api_view(['GET','POST'])
# def products_list(request):

#     if request.method == 'GET':
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET','PUT','DELETE'])
# def product_details(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)