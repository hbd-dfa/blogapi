# Generated by Django 3.0.3 on 2021-01-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='crated_at',
            new_name='created_at',
        ),
    ]