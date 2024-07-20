from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Recipe


class ListRecipes(ListView):
    """
        List all recpies available.
    """
    model = Recipe
    template_name = 'recipe_list.html'

class CreateRecipe(CreateView):
    """
        Creates a recpie
    """
    model = Recipe
    fields = ('__all__')
    template_name = 'create_recpie.html'