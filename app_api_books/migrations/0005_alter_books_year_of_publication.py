# Generated by Django 5.0.6 on 2024-06-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api_books', '0004_books_year_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='year_of_publication',
            field=models.IntegerField(),
        ),
    ]