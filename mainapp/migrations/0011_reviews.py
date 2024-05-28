# Generated by Django 4.2.10 on 2024-05-28 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('review', models.CharField(max_length=255)),
                ('cus_rating', models.ImageField(blank=True, default=0, null=True, upload_to='')),
            ],
        ),
    ]
