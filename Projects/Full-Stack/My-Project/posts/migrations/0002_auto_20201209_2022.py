# Generated by Django 3.1.4 on 2020-12-09 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_update',
            new_name='updated_at',
        ),
    ]