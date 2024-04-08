from django.db import models

class CustomerReview(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    flag = models.URLField(max_length=100, null=True, blank=True)
    reviews = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name