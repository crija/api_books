# Generated by Django 5.0.6 on 2024-06-04 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_api_books', '0002_books_number_of_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='number_of_pages',
            field=models.IntegerField(max_length=10),
        ),
    ]
