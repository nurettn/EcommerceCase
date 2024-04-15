from django.db import models


class UserInformation(models.Model):
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=False)


class StoreInformation(models.Model):
    user = models.ForeignKey(
        UserInformation,
        on_delete=models.CASCADE,
        related_name="stores",
        blank=False,
    )
    store_url = models.URLField(blank=False)
    PLATFORM_CHOICES = [
        ("trendyol", "Trendyol"),
        ("hepsiburada", "Hepsiburada"),
        ("amazon", "Amazon"),
    ]
    platform = models.CharField(
        max_length=20, choices=PLATFORM_CHOICES, blank=False
    )
