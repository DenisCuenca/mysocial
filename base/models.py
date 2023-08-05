from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
