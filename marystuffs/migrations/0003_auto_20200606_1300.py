# Generated by Django 3.0.6 on 2020-06-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marystuffs', '0002_auto_20200602_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='loc_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='zipcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
