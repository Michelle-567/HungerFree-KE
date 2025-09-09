from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'food_item', 'quantity', 'expiry_date', 'location', 'created_at')
    list_filter = ('expiry_date', 'location')
    search_fields = ('food_item', 'donor__username')
