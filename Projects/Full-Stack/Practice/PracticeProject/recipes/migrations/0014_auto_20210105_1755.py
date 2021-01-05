# Generated by Django 3.1.4 on 2021-01-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_auto_20210105_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='difficulty_type',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Hard', 'Hard')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='flavor_type',
            field=models.CharField(choices=[('Sour', 'Sour'), ('Sweet', 'Sweet'), ('Salty', 'Salty')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method_type',
            field=models.CharField(choices=[('Cook', 'Cook'), ('Bake', 'Bake')], max_length=50),
        ),
    ]
