# Generated by Django 3.1.4 on 2021-01-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='difficulty_type',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='method_type',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='flavor_type',
            field=models.CharField(choices=[('Sour', 'Sour'), ('Sweet', 'Sweet'), ('Salty', 'Salty')], max_length=50),
        ),
    ]