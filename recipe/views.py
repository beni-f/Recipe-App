from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, InlineFormSetView
from .models import Recipe, RecipeNutrition
from .forms import RecipeForm

class NutritionInline(InlineFormSetFactory):
    model = RecipeNutrition
    fields = ('__all__')
    factory_kwargs = {'max_num': 1}

class ListRecipes(ListView):
    """
        List all recpies available.
    """
    model = Recipe
    template_name = 'recipe_list.html'

class CreateRecipe(CreateWithInlinesView):
    """
        Creates a recpie
    """
    model = Recipe
    form_class = RecipeForm
    inlines = [NutritionInline]
    template_name = 'create_recpie.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        return super().form_valid(form)

class DetailRecipe(DetailView):
    """
        Displays the details for a recipe
    """
    model = Recipe
    template_name = 'recipe_detail.html'

class UpdateRecipe(UpdateWithInlinesView):
    """
        Updates a Recipe
    """
    model = Recipe
    fields = ('__all__')
    inlines = [NutritionInline]
    template_name = 'recipe_update.html'

class DeleteRecipe(DeleteView):
    model = Recipe
    success_url = 'recipes'
    template_name = 'recipe_delete.html'
