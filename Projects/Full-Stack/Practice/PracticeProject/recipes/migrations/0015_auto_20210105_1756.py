# Generated by Django 3.1.4 on 2021-01-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_auto_20210105_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]