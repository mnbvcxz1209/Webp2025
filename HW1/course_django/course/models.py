from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    department = models.CharField(max_length=100)
    coursetitle = models.CharField(max_length=100,default="Unknown coursetitle")
    instructor = models.CharField(max_length=100,default="Unknown Instructor")
    created_at = models.DateTimeField(auto_now_add=True)

