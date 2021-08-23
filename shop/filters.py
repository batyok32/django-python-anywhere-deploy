from django_filters import rest_framework as filters
from .models import Product, Category, Subcategory, Brand
from django_filters.fields import Lookup
from django_filters import Filter
from django.db.models import Q
from django.utils import timezone
import datetime


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(
        field_name="new_price", lookup_expr='gte')
    max_price = filters.NumberFilter(
        field_name="new_price", lookup_expr='lte')

    min_dis = filters.NumberFilter(field_name="discount", lookup_expr='gte')
    max_dis = filters.NumberFilter(field_name="discount", lookup_expr='lte')
   
    category_id = filters.NumberFilter(field_name="category__id", lookup_expr='exact')
    # search = filters.CharFilter(field_name="translations__name", lookup_expr="icontains")
    
    subcategory_ids = filters.ModelMultipleChoiceFilter(queryset=Subcategory.objects.all(), to_field_name='id', field_name='subcategory__id')
    brand_ids = filters.ModelMultipleChoiceFilter(queryset=Brand.objects.all(), to_field_name='id', field_name='brand__id')
    new = filters.BooleanFilter(method='was_recent')

    def was_recent(self, queryset, name, value):
        now = timezone.now()
        if value == True:
            query = queryset.filter(Q(created__gt=now - datetime.timedelta(days=7)) & Q(created__lt=now))
            if len(query) == 0:
                return queryset.order_by('created')
            return query
        else:
            return queryset
    

    class Meta:
        model = Product
        fields = ['discount']

class BrandFilter(filters.FilterSet):

    class Meta:
        model = Brand
        fields = ['category']


class SearchingFilter(filters.FilterSet):
    category_id = filters.NumberFilter(field_name="category__id", lookup_expr='exact')
    name = filters.CharFilter(field_name="translations__name", lookup_expr="icontains")
    new = filters.BooleanFilter(method='was_recent')

    def was_recent(self, queryset, name, value):
        now = timezone.now()
        if value == True:
            return queryset.filter(Q(created__gt=now - datetime.timedelta(days=7)) & Q(created__lt=now))
        else:
            return queryset
    

    class Meta:
        model = Product
        fields =['discount']


# For Dynamic Search
# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])



# TODO: COMMENT FILTER
# def departments(request):
#     if request is None:
#         return Department.objects.none()

#     company = request.user.company
#     return company.department_set.all()

# class EmployeeFilter(filters.FilterSet):
#     department = filters.ModelChoiceFilter(queryset=departments)



# FUNCTION FILTER
#  find_anywhere = filters.CharFilter(method='look_anywhere')
    # def look_anywhere(self, queryset, name, value):
    #     return queryset.filter(Q(name__icontains=value) | Q(description__icontains=value))


# with_discount = filters.BooleanFilter(method='get_discount')
    # def get_discount(self, queryset, name, value):
    #     return queryset.filter(discount )
    #TODO: When postgres is linked open this
    # def filter_search(self, queryset, name, value):
    #     return queryset.annotate(search=SearchVector('name', 'description')).filter(search=value)

# search = filters.CharFilter(method='filter_search')
    # category_ids = filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), to_field_name='id', field_name='category__id')
    # subcategory_id = filters.CharFilter(field_name="subcategory__id", lookup_expr='exact')

 # o = filters.OrderingFilter(
    #     # tuple-mapping retains order
    #     fields=(
    #         ('new_price', 'price'),
    #         ('created', 'created')

    #     ),

    #     # labels do not need to retain order
    #     field_labels={
    #         'price': 'Sort price ',
    #     }
    # )