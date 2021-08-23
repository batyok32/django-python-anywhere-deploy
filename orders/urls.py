from django.urls import path
from . import views


urlpatterns = [
    path('delete/', views.OrderDeleteView.as_view()),
    path('products/<int:pk>/', views.OrderProducts.as_view()),
    path('', views.OrderListCreateView.as_view()),
]


