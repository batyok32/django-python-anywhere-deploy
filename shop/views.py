# Django feauteres
from django.shortcuts import  get_object_or_404
from django.utils import timezone


# Models
from .models import Category, Product, Comment, Subcategory, Brand, Coupon

# Serializers
from .serializers import ProductSerializer, CommentListSerializer, \
    CategorySerializer, SubcategorySerializer, \
    BrandSerializer, CouponSerializer, \
    AccountInfoSerializer, SearchSerializer, ProductDetailSerializer

# RESTFRAMEWORK stuff
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Filters
from django_filters import rest_framework as filters
from .filters import ProductFilter, BrandFilter, SearchingFilter
from rest_framework.filters import SearchFilter, OrderingFilter

# Recommendation
from .recommendation import get_reccommendation

# Pagination
from .pagination import MyOffsetPagination
# Parler
from django.utils.translation import get_language_from_request


# List Products
class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['$translations__name']
    ordering_fields = ['new_price', 'created']
    pagination_class = MyOffsetPagination

    def get_queryset(self):
        lang_code = get_language_from_request(self.request)
        query = Product.objects.language(lang_code).filter(available=True)
        return query

class SearchProducts(generics.ListAPIView):
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = SearchingFilter
    search_fields = ['$translations__name']
    pagination_class = MyOffsetPagination
    serializer_class=SearchSerializer

    def get_queryset(self):
        lang_code = get_language_from_request(self.request)
        query = Product.objects.language(lang_code).filter(available=True)
        return query
    

# List Categories
class CategoryList(generics.ListAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyOffsetPagination


    def get_queryset(self):
        lang_code = get_language_from_request(self.request)
        query = Category.objects.language(lang_code).all()
        return query


# List Subcategories
class SubcategoryList(generics.ListAPIView):
    serializer_class = SubcategorySerializer
    pagination_class = MyOffsetPagination

    def get_queryset(self):
        category_id = self.kwargs['pk']
        lang_code = get_language_from_request(self.request)
        return Subcategory.objects.language(lang_code).filter(category__id=category_id)

# List Brands
class BrandList(generics.ListAPIView):
    serializer_class = BrandSerializer
    # queryset = Brand.objects.all()
    pagination_class = MyOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BrandFilter

    def get_queryset(self):
        lang_code = get_language_from_request(self.request)
        query = Brand.objects.language(lang_code).all()
        return query

# Retrieve Product
class ProductDetail(generics.RetrieveAPIView):
    # queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        lang_code = get_language_from_request(self.request)
        query = Product.objects.language(lang_code).filter(available=True)
        return query
    
    def get_object(self):
        queryset = self.get_queryset()
        filter_query = {}
        filter_query['id'] = self.kwargs['pk']
        obj = get_object_or_404(queryset, **filter_query)
        self.check_object_permissions(self.request, obj)
        
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = Response(serializer.data)
        response.set_cookie('products', [instance.id])
        return response

# List and add Comments
class CommentList(generics.ListCreateAPIView):
    pagination_class = MyOffsetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class=CommentListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        product = Product.objects.get(id=self.kwargs['pk'])
        serializer.save(user=self.request.user, product=product)


    def get_queryset(self):
        prd_id = self.kwargs['pk']
        return Comment.objects.filter(product__id=prd_id)

# Check coupon is valid or not
class CouponCheckView(APIView):
    """
    Check coupon is active or not
    """
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        code = request.data['coupon']
        find = get_object_or_404(Coupon.objects.all(), code=code, valid_to__gt=timezone.now())
        serializer = CouponSerializer(find)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get account additional information
class AccountInfoList(APIView):
    """
    Response account info
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer=AccountInfoSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class Recommend(APIView):

    def get(self, request, *args, **kwargs):
        #print("Recommending started")
        prPk = self.kwargs['pk']
        lang_code = get_language_from_request(request)
        #print(f"Lang:{lang_code} pk: {prPk}")
        res = get_reccommendation(prPk, lang_code)
        #print("Response", res)
        products = Product.objects.language(lang_code).filter(id__in=res)
        #print("Products", products)
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


