from django.db import models

class FaqSection(models.Model):
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.question
    