from django.urls import path
from . import views


urlpatterns = [
    path('', views.SliderList.as_view()),
]