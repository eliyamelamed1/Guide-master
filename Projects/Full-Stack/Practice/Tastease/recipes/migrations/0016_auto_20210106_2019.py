# Generated by Django 3.1.4 on 2021-01-06 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_remove_recipe_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
