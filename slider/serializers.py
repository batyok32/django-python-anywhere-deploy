from rest_framework import serializers
from .models import Slider


class SliderSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    
    def get_picture(self, obj):
        return self.context['request'].build_absolute_uri( obj.picture.url)

    class Meta:
        model = Slider
        fields = ('id', 'name', 'picture', 'link')
