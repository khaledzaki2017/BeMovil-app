# Generated by Django 2.1.3 on 2020-09-05 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200904_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpictures',
            name='user_uuid',
        ),
    ]