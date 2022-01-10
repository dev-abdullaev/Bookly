# Generated by Django 4.0 on 2022-01-09 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main_app', '0012_remove_book_favorites_favorite_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
            preserve_default=False,
        ),
    ]
