# Generated by Django 3.1.13 on 2021-11-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='fuel',
            field=models.CharField(choices=[('CNG', 'CNG'), ('DIESEL', 'DIESEL'), ('PETROL', 'PETROL')], max_length=50),
        ),
    ]
