# Generated by Django 3.1.4 on 2021-01-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20210106_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
