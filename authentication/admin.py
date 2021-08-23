from django.contrib import admin
from .models import UserAccount
from django.utils.safestring import mark_safe


def profile_avatar(self):
    if self.profile_avatar:
        return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" height="40" width="40"/></a>'.format(self.profile_avatar.url))
    else:
        return '(Нет изображения)'


profile_avatar.short_description = 'Картинка'
profile_avatar.allow_tags = True


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'city',
                profile_avatar, 'is_staff', 'is_active', 'date_joined']
    list_filter = ['username', 'phone_number', 'date_joined']
    readonly_fields = ['date_joined']
    model = UserAccount

    fieldsets = (
        ("Profile", {
            'fields': (
                'username',
                'phone_number',
                'address',
                'city',
                'email',
                'profile_img',
                'password',
            )
        }),
        ("Permissions", {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'last_login',
                'groups',
                'user_permissions',
                'date_joined'
            )
        })
    )


admin.site.register(UserAccount, CustomUserAdmin)
