# Generated by Django 4.0 on 2022-01-10 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_blog_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='added_date',
            new_name='created_date',
        ),
    ]
