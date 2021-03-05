from django.db import models


# Create your models here.
class events(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    published = models.BooleanField(default=False)
def  __str__(self):
    return self.title
