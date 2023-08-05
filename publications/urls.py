from django.urls import path
from .views import  Feed, create_post
urlpatterns = [
    path("", Feed.as_view(), name = "feed"),
    path("create_post", create_post, name="create_post")
]