# Generated by Django 3.1.4 on 2021-01-05 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_auto_20210105_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='method_type',
            field=models.CharField(choices=[('Cook', 'Cook'), ('Bake', 'Bake')], max_length=50),
        ),
    ]
