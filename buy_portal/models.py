from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime
import os

CAT_CHOICES = (
    ('Other', 'Other'),
    ('Book', 'Book'),
    ('Instrument', 'Instrument'),
    ('Project', 'Project'),
)


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Item(models.Model):
    category = models.CharField(max_length=10, choices=CAT_CHOICES, default='Other')
    item_name=models.CharField(max_length=100)
    mrp_price=models.IntegerField()
    selling_price=models.IntegerField()
    image=models.FileField()
    description=models.CharField(max_length=100)
    datetime=models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)

class Requirement(models.Model):
    user = models.ForeignKey(User, default=1,on_delete= models.CASCADE)
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    expected_price = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.now, blank=True)

class Advertisement(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.FileField()
    datetime = models.DateTimeField(default=datetime.now, blank=True)






