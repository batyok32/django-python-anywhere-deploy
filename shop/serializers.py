# Rest Framework   
from rest_framework import serializers
# Models
from .models import Product, Category, Comment, Brand, Subcategory, \
 Coupon
from django.contrib.auth import get_user_model

# Parler
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from .serializersMixins import TranslatedSerializerMixin


class CategorySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    picture = serializers.SerializerMethodField()
    translations = TranslatedFieldsField(shared_model=Category)

    def get_picture(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture.url)

    class Meta:
        model = Category
        fields = ('id', 'translations', 'slug','picture')

class SubcategorySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    category = CategorySerializer(read_only=True)
    translations = TranslatedFieldsField(shared_model=Subcategory)

    class Meta:
        model = Subcategory
        fields = ('id', 'translations', 'slug', 'category')


class BrandSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Brand)
    picture = serializers.SerializerMethodField()
    
    def get_picture(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture.url)

    class Meta:
        model = Brand
        fields = ('id', 'translations', 'slug', 'picture')


class ProductSerializer(TranslatableModelSerializer):
    # translations = TranslatedFieldsField(shared_model=Product)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    # Own fields
    new = serializers.BooleanField(source='was_published_recently')
    old_price = serializers.DecimalField(
        source='price', max_digits=10, decimal_places=2)
  
    # Method Fields
    picture_middle = serializers.SerializerMethodField()
    picture_search = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'category', 'brand',
        'name', 'slug', 'old_price', 'new_price', 
        'picture_middle','picture_search',
        'amount', 'discount',
        'new', 'sold')
        model = Product
    

    def get_picture_middle(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_middle.url)
    
    def get_picture_search(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_search.url)
    
   

class ProductDetailSerializer(TranslatableModelSerializer):
    # Foreign KEy Fields
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    
    # Own fields
    new = serializers.BooleanField(source='was_published_recently')
    old_price = serializers.DecimalField(
        source='price', max_digits=10, decimal_places=2)
   
    # Method Fields
    picture_large = serializers.SerializerMethodField()
    picture_middle = serializers.SerializerMethodField()
    picture_search = serializers.SerializerMethodField()

    class Meta:
        fields = (
        'id', 'name', 'slug', 'description', 'category',
        'brand','old_price', 'new_price', 
        'picture_large','picture_middle', 'picture_search', 
        'amount', 'discount',
        'created', 'new', 'sold'
        )
        model = Product
    

    def get_picture_large(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_large.url)
    
    def get_picture_middle(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_middle.url)
    
    def get_picture_search(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_search.url)
    
class SearchSerializer(TranslatableModelSerializer):
    picture_search = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'name', 'slug', 'picture_search', 'new_price')
        model = Product

    def get_picture_search(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture_search.url)
    


class UserSerializer(serializers.ModelSerializer):
    profile_avatar = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'profile_avatar'
        )
    def get_profile_avatar(self, obj):
        return self.context['request'].build_absolute_uri( obj.profile_avatar.url)
    


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'product','user', 'body', 'created')
        read_only_fields = ('id', 'product','user', 'created')

class CouponSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Coupon
        fields = ('id', 'code', 'discount')




class AccountInfoSerializer(serializers.ModelSerializer):
    total_shop = serializers.DecimalField(source='get_total_shop', max_digits=10, decimal_places=2)
    comments_count = serializers.IntegerField(source='get_comments_count')
    total_products = serializers.IntegerField(source='get_total_products')
    total_orders=serializers.IntegerField(source='get_total_orders')

    class Meta:
        model=get_user_model()
        fields = ('username','total_shop', 'comments_count', 'total_products', 'total_orders')
        read_only_fields= ['username', 'total_shop', 'comments_count', 'total_products', 'total_orders']
    
    

