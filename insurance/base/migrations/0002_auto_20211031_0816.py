# Generated by Django 3.1.13 on 2021-10-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='date_of_purchase',
            field=models.DateField(),
        ),
    ]