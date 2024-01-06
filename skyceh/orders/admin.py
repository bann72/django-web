from django.contrib import admin

# Register your models here.

from .models import MainOrderInfo


class MOIAdmin(admin.ModelAdmin):
    list_display = ("znum", "prod", "invorder")
    list_filter = ("prod", "client")
    fields = [("znum", "prod", "count"), ("client", "invorder", "lastday")]


admin.site.register(MainOrderInfo, MOIAdmin)
