# Generated by Django 3.1.4 on 2021-01-06 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_recipe_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='is_published',
        ),
    ]
