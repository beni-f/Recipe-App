# Generated by Django 5.0.7 on 2024-07-22 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_rename_recipe_recipenutrition_recipe_for_nutirent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='nutrition',
            new_name='nutrition_id',
        ),
        migrations.RenameField(
            model_name='recipenutrition',
            old_name='recipe_for_nutirent',
            new_name='recipe_id',
        ),
    ]
