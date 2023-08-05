from django.contrib import admin
from .models import  Comment, Publication
# Register your models here.

admin.site.register(Comment)
admin.site.register(Publication)