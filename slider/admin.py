from django.contrib import admin
from .models import Slider
from django.utils.safestring import mark_safe
from django.contrib.admin import AdminSite

def slider_img(self):
    if self.picture_admin:
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" height="100" width="100"/></a>'.format(self.picture_admin.url))
    else:
        return '(Нет изображения)'


slider_img.short_description = 'Картинка'
slider_img.allow_tags = True


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', slider_img)
    search_fields = ['name','link']

