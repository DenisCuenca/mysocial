from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, TemplateView

from publications.models import Publication


# Create your views here.
class Feed(ListView):
    template_name = "publications/feed.html"
    model = Publication


def create_post(request):
    if request.method == "POST":

        print(type(request.FILES["image"]))
        print(type(request.POST["contenido"]))
        Publication(description=request.POST["contenido"], media=request.FILES["image"], created_by=request.user).save()


