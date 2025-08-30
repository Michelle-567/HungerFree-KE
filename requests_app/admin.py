from django.contrib import admin
from .models import FoodRequest

@admin.register(FoodRequest)
class FoodRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "requester", "donation", "quantity", "status", "created_at")
    list_filter = ("status", "created_at")
