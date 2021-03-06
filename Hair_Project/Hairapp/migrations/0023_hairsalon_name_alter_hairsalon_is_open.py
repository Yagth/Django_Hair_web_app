# Generated by Django 4.0.3 on 2022-03-13 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairapp', '0022_remove_hairsalon_available_services_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairsalon',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='hairsalon',
            name='is_open',
            field=models.CharField(choices=[('O', 'Opened'), ('C', 'Closed')], default='C', max_length=1),
        ),
    ]
