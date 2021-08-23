from django.utils.safestring import mark_safe

def product_img(self):
    if self.picture_search:
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" style="border-radius:15px;" height="90" width="120"/></a>'.format(self.picture_search.url))
    else:
        return '(Нет изображения)'


product_img.short_description = 'Картинка'
product_img.allow_tags = True

def category_img(self):
    if self.picture:
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" style="border-radius:15px; height="100" width="150"/></a>'.format(self.picture.url))
    else:
        return '(Нет изображения)'


category_img.short_description = 'Картинка'
category_img.allow_tags = True