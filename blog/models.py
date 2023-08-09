from django.db import models
class post(models.Model):
    Tittle=models.CharField(max_length=50)
    desc=models.TextField()

# Create your models here.
