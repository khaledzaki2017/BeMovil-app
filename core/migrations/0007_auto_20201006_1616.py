# Generated by Django 2.2 on 2020-10-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201006_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizardformjuridica',
            name='id_image1',
            field=models.ImageField(null=True, upload_to='user_images/id_images'),
        ),
    ]
