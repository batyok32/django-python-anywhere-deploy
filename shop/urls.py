from django.urls import path
from . import views


urlpatterns = [
    path('comments/<int:pk>/', views.CommentList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('products/', views.ProductList.as_view()),
    path('search/', views.SearchProducts.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('brands/', views.BrandList.as_view()),
    path('coupon/', views.CouponCheckView.as_view()),
    path('subcategories/<int:pk>/', views.SubcategoryList.as_view()),
    path('account/info/', views.AccountInfoList.as_view()),
    path('recommend/<int:pk>/', views.Recommend.as_view())
]
