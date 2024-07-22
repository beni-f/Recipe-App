from django.shortcuts import render
from django.views.generic import TemplateView
from recipe.views import ListRecipes

# Create your views here.
class HomePageView(ListRecipes):
    template_name = "home.html"
