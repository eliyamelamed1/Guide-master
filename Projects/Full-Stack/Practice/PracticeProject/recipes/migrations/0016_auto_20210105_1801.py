# Generated by Django 3.1.4 on 2021-01-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20210105_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='method_type',
            field=models.CharField(choices=[('---', 'Any'), ('Cook', 'Cook'), ('Bake', 'Bake')], default='---', max_length=50),
        ),
    ]
