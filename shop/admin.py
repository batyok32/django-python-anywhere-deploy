from django.contrib import admin
from .models import Category, Product, Comment, Contact, Size, Brand, Subcategory, Coupon
from django.contrib.admin import AdminSite
from .adminImg import product_img, category_img
from parler.admin import TranslatableAdmin



AdminSite.site_url = "/api/v0/products/"
AdminSite.site_header = "DAVIDO ADMIN"


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',category_img, 'slug')
    # prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    fieldsets = (
        ("Category Information", {
            'fields': (
                'name',
                'slug',
                'image'
            )
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

class SizeInline(admin.TabularInline):
    model=Size
    extra=1


@admin.register(Subcategory)
class SubcategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'category')
    # prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    fieldsets = (
        ("Subcategory Information", {
            'fields': (
                'name',
                'slug',
                'category',
                'image'
            )
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    fieldsets = (
        ("Product Information", {
            'fields': (
                'name',
                'description',
                'category',
                'subcategory',
                'price',
                'amount',
                'discount',
                'brand',
            )
        }),
        ("Additional Information", {
            'fields': (
                'slug',
                'new_price',
                'available',
                'sold',
                'created',
                'updated'
            ),
            'classes': ('collapse',)
        }),
        ("Images", {
            'fields': (
                'image',

            ),
        }),

    )
    list_display = ['name', product_img, 'sold', 'amount', 'new_price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['new_price', 'available']
    autocomplete_fields = ['category', 'subcategory']
    search_fields=['name']
    # prepopulated_fields = {'slug': ('name',), }
    readonly_fields = ['created', 'updated']
    inlines=[SizeInline,]


    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ['user__username', 'body']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created')
    list_filter = ['created']
    search_fields = ('name', 'phone_number', 'body')


@admin.register(Brand)
class BrandAdmin(TranslatableAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']
    # prepopulated_fields = {'slug': ('name',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to',
                'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']


    