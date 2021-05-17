from django.db import models

# Create your models here.

class URL(models.Model):
    original_url =models.CharField(max_length=200, unique=True)
    shortened_url = models.CharField(max_length=200, unique=True, default=None)

    def __str__(self):
        return self.original_url
