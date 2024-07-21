from .models import Recipe
from django import forms
from datetime import timedelta

HOURS_CHOICES = [(i, f'{i} hour') for i in range(24)]
MINUTES_CHOICES = [(i, f'{i} minutes') for i in range(60)]

class RecipeForm(forms.ModelForm):
    cooking_time_hours = forms.ChoiceField(choices=HOURS_CHOICES, required=False, initial=0)
    cooking_time_minutes = forms.ChoiceField(choices=MINUTES_CHOICES, required=False, initial=0)

    class Meta:
        model = Recipe
        fields = ('__all__')
    
    def clean(self):
        cleaned_data = super().clean()
        cooking_time_hours = int(cleaned_data.get('cooking_time_hours', 0))
        cooking_time_minutes = int(cleaned_data.get('cooking_time_minutes', 0))

        cooking_time = timedelta(hours=cooking_time_hours, minutes=cooking_time_minutes)
        cleaned_data['cooking_time'] = cooking_time

        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        cooking_time_hours = int(self.cleaned_data.get('cooking_time_hours', 0))
        cooking_time_minutes = int(self.cleaned_data.get('cooking_time_minutes', 0))
        instance.cooking_time = timedelta(hours=cooking_time_hours, minutes=cooking_time_minutes)

        if commit:
            instance.save()
        return instance