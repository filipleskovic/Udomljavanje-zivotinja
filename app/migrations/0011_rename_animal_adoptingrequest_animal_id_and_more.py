# Generated by Django 5.0.4 on 2024-06-05 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_user_is_active_user_is_staff_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adoptingrequest',
            old_name='animal',
            new_name='animal_id',
        ),
        migrations.RenameField(
            model_name='adoptingrequest',
            old_name='user',
            new_name='user_id',
        ),
    ]
