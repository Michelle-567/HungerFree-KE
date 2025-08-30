from django.db import models
from accounts.models import User

class FoodDonation(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("claimed", "Claimed"),
        ("delivered", "Delivered"),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donations")
    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.CharField(max_length=50)
    expiry_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
