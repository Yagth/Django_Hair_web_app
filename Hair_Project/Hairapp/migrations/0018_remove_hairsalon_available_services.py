# Generated by Django 4.0.3 on 2022-03-12 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0017_rename_image_hairsalon_salon_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hairsalon',
            name='Available_services',
        ),
    ]