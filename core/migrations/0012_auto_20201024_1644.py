# Generated by Django 2.2 on 2020-10-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201024_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizardformjuridica',
            name='number',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='wizardformnatural',
            name='number',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
