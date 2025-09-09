from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("donor", "Donor"),
        ("recipient", "Recipient"),
        ("volunteer", "Volunteer/Driver"),
        ("admin", "Admin"),
    ]
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="recipient")
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    availability = models.CharField(max_length=100, help_text="When are you available?")
    skills = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
