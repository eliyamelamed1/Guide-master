# Generated by Django 3.1.4 on 2021-01-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_auto_20210105_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='method_type',
            field=models.CharField(choices=[('---s', 'Any'), ('Cook', 'Cook'), ('Bake', 'Bake')], default='---s', max_length=50),
        ),
    ]