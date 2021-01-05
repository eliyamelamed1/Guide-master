# Generated by Django 3.1.4 on 2021-01-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20210105_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty_type',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Hard', 'Hard')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='flavor_type',
            field=models.CharField(choices=[('Sour', 'Sour'), ('Sweet', 'Sweet'), ('Salty', 'Salty')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method_type',
            field=models.CharField(choices=[('Cook', 'Cook'), ('Bake', 'Bake')], default=None, max_length=50),
        ),
    ]