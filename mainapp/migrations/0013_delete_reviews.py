# Generated by Django 4.2.10 on 2024-05-28 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_remove_reviews_cus_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
