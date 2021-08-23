# Not working because its already included in config urls

from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import ObtainTokenPairWithColorView
from django.conf.urls import url

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(),
        name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
