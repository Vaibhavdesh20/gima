from django.contrib import admin
from .models import iplist
# Register your models here.


class IPAdmin(admin.ModelAdmin):
    list_display = ("group", "ip_address","site","dept","user_name","mac_address",)

admin.site.register(iplist,IPAdmin )
