from django.db import models
from django.conf import settings
from donations.models import Donation

class FoodRequest(models.Model):
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    donation = models.ForeignKey(
        Donation,
        on_delete=models.CASCADE,
        related_name="requests"
    )
    quantity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester} requested {self.quantity} of {self.donation.food_item}"

from django.db import models

class HelpRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200)
    reason = models.TextField(help_text="Why are you requesting help?")
    urgent = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
