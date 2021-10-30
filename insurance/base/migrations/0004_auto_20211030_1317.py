# Generated by Django 3.1.13 on 2021-10-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211030_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='income_group',
            field=models.CharField(choices=[('0-25k', '0-$25k'), ('>$70', '>$70K'), ('$25-$70', '$25-$70K')], max_length=50),
        ),
        migrations.AlterField(
            model_name='policy',
            name='vehicle_segment',
            field=models.CharField(choices=[('A', 'A'), ('B', 'A'), ('C', 'A')], max_length=50),
        ),
    ]
