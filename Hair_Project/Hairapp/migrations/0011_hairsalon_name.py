# Generated by Django 4.0.3 on 2022-03-12 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0010_hairsalon_rators_hairsalon_total_customers'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairsalon',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
