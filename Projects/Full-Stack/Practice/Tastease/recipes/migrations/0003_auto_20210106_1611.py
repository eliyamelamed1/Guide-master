# Generated by Django 3.1.4 on 2021-01-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210106_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
