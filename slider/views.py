from .models import Slider
from shop.views import MyOffsetPagination
# RESTFRAMEWORK
from rest_framework import generics
from .serializers import SliderSerializer


class SliderList(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    pagination_class = MyOffsetPagination
