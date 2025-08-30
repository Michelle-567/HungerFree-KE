from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "sent_at")
    list_filter = ("sent_at",)
    search_fields = ("user__username", "message")

admin.site.register(Notification, NotificationAdmin)
