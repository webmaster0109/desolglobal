from django.db import models

def generate_default_title(instance, prefix):
    return f"{prefix} {instance.pk}" if instance.pk else f"{prefix} {instance.__class__.__name__}"

class BaseMedia(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='desol/images/', null=True, blank=True)
    alt_text = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title or generate_default_title(self, 'Media')

    class Meta:
        abstract = True

class Logo(BaseMedia):
    def __str__(self):
        return self.title or generate_default_title(self, 'Logo')

class Favicon(BaseMedia):
    def __str__(self):
        return self.title or generate_default_title(self, 'Favicon')

class SocialMediaLinks(BaseMedia):
    link = models.URLField(max_length=255, null=True, blank=True)
    def upload_to_path(instance, filename):
        return f"desol/images/social/{instance.title}/{filename}"
    image = models.ImageField(upload_to=upload_to_path, null=True, blank=True, verbose_name='Social Image')

    def __str__(self):
        return self.title or generate_default_title(self, 'Social Media')
    
    def save(self, *args, **kwargs):
        if not self.alt_text:
            self.alt_text = f"Desol Social {self.title}" if self.title else "Desol Social Media"
        super().save(*args, **kwargs)

class GoogleMapEmbed(models.Model):
    embed_code = models.TextField(default="", null=True, blank=True)
    def __str__(self):
        return generate_default_title(self, 'Embed Map')
    
