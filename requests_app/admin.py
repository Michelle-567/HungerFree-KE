from django.contrib import admin
from .models import FoodRequest

class FoodRequestAdmin(admin.ModelAdmin):
    list_display = ("food_item", "recipient", "status", "requested_at")
    list_filter = ("status", "requested_at")
    search_fields = ("food_item__title", "recipient__username")

admin.site.register(FoodRequest, FoodRequestAdmin)
