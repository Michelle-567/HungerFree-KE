from django.db import models
from django.conf import settings

class Donation(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_item} by {self.donor}"
