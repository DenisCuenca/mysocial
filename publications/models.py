from django.db import models
from base.models import  ModelBase
# Create your models here.

class Publication(ModelBase):
    description = models.CharField(max_length=250)
    media = models.FileField(null = True, blank=True, upload_to="post/")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.created_by.username} - {self.created_at}"


class Comment(ModelBase):
    content = models.CharField(max_length=200)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.created_by} - {self.created_at}"
