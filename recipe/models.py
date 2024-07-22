from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Courses(models.Model):
    """
        Course Model
    """
    course_name = models.CharField(max_length=32)

    def __str__(self):
        return self.course_name
    
def get_default_course():
    return Courses.objects.get(course_name='Others').id

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    serving_size = models.IntegerField()
    cooking_time = models.DurationField(null=True)
    ingredients = models.TextField()
    directions = models.TextField(null=True, blank=True)
    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        default=get_default_course
    )
    nutrition = models.ForeignKey(
        'RecipeNutrition',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipes")

class Groceries(models.Model):
    grocery = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

class RecipeNutrition(models.Model):
    calories = models.FloatField()
    total_fat = models.FloatField()
    saturated_fat = models.FloatField()
    cholesterol = models.FloatField()
    total_carbohydrate = models.FloatField()
    dietary_fiber = models.FloatField()
    sugars = models.FloatField()
    protien = models.FloatField()
    recipe_id = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=True,
    )
