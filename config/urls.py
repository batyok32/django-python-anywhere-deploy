# Admin
from django.contrib import admin

# Url
from django.urls import path, include

# Rest Docs
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# Settings
from django.conf import settings
from django.conf.urls.static import static

# Rest framework
from rest_framework import permissions



# schema_view = get_schema_view(
#     openapi.Info(
#         title="Blog API",
#         default_version="v1",
#         description="A sample API for learning DRF",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="hello@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v0/sliders/", include("slider.urls")),
    path("api/v0/orders/", include("orders.urls")),
    path("api/v0/", include("shop.urls")),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# path('swagger/', schema_view.with_ui(  # new
    #     'swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui(  # new
    #     'redoc', cache_timeout=0), name='schema-redoc'),