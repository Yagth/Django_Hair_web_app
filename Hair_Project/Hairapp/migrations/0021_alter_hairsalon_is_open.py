# Generated by Django 4.0.3 on 2022-03-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0020_hairsalon_is_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hairsalon',
            name='is_open',
            field=models.CharField(default='CLOSED', max_length=100),
        ),
    ]
