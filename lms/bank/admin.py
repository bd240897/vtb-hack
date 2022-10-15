from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(VtbGroup)
class VtbGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "get_users_count", )
    readonly_fields = ("owner",)
    save_on_top = True
    save_as = True

    def get_users_count(self, obj):
        return obj.users.all().count()

    get_users_count.short_description = "Число участников"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "status", "get_image")
    list_editable = ("status",)
    list_filter = ("status", )
    search_fields = ("user__username", "name",)
    # чтоб показать фотку внутри профиля
    readonly_fields = ("user", "get_image",)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="50" height="60"')

    get_image.short_description = "Аватар"

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "publicKey", "privateKey")
    readonly_fields = ("user",)
    search_fields = ("user__username",)
    save_on_top = True
    save_as = True