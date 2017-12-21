from django.db import models

# Create your models here.
class Advices(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.title
