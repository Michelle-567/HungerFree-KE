from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "donor", "food_item", "quantity", "expiry_date", "location", "created_at")
    list_filter = ("expiry_date", "created_at")
