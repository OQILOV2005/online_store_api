from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


@admin.register(models.User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone','avatar')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Sub_Category)
admin.site.register(models.Saved)
admin.site.register(models.Comment)
admin.site.register(models.Order)
admin.site.register(models.Tag)
admin.site.register(models.ProductImage)
admin.site.register(models.Region)

