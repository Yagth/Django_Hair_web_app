# Generated by Django 4.0.3 on 2022-03-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0014_alter_hairsalon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hairsalon',
            name='Available_services',
            field=models.CharField(choices=[('None', 'None')], default=('None', 'None'), max_length=10),
        ),
    ]
