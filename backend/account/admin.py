from django.contrib import admin
from .models import AccountUser


@admin.register(AccountUser)
class AccountUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "first_name", "last_name", "is_staff")
    search_fields = ("email", "username", "first_name", "last_name")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("-date_joined",)
