from django.db import models

# Create your models here.

class EndPoints(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.name}"