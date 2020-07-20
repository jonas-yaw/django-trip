from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Suggest


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class SuggestPageView(CreateView):
    template_name = "suggest.html"
    model = Suggest
    fields = ("suggestion",)


class SuggestDonePageView(TemplateView):
    template_name = "suggest_done.html"

