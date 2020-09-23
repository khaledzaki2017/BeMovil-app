# Generated by Django 2.2 on 2020-09-21 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('otp', models.CharField(max_length=6)),
                ('initial', models.IntegerField(blank=True, null=True)),
                ('last', models.IntegerField(blank=True, null=True)),
                ('validated', models.BooleanField(default=False)),
                ('count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WizardForm',
            fields=[
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False, unique=True)),
                ('_type', models.CharField(choices=[(1, 'Natural'), (2, 'Juridica')], max_length=100)),
                ('personal_id', models.TextField(max_length=250, null=True)),
                ('firstname', models.CharField(max_length=250, null=True)),
                ('lastname', models.CharField(max_length=250, null=True)),
                ('bemovil_id', models.IntegerField(null=True)),
                ('expedition_date', models.DateField(null=True)),
                ('expedition_place', models.CharField(max_length=250, null=True)),
                ('mobile_phone', models.IntegerField(null=True)),
                ('number', models.IntegerField(null=True)),
                ('address', models.TextField(max_length=250, null=True)),
                ('city', models.CharField(max_length=250, null=True)),
                ('valley', models.CharField(max_length=250, null=True)),
                ('company_name', models.CharField(max_length=250, null=True)),
                ('actividad_economica', models.CharField(max_length=250, null=True)),
                ('direccion', models.TextField(max_length=250, null=True)),
                ('barrio', models.CharField(max_length=250, null=True)),
                ('ciudad', models.CharField(max_length=250, null=True)),
                ('departamento', models.CharField(max_length=250, null=True)),
                ('telefono_fijo', models.IntegerField(blank=True, null=True)),
                ('ingresos', models.IntegerField(blank=True, null=True)),
                ('total_activos', models.IntegerField(blank=True, null=True)),
                ('egresos', models.IntegerField(blank=True, null=True)),
                ('total_pasivos', models.IntegerField(blank=True, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('uploader', models.CharField(max_length=250, null=True)),
                ('firstFile', models.FileField(upload_to='documents')),
                ('secondFile', models.FileField(upload_to='documents')),
                ('file', models.BinaryField(null=True)),
                ('id_image1', models.ImageField(null=True, upload_to='user_images/id_images')),
                ('id_image2', models.ImageField(null=True, upload_to='user_images/id_images')),
                ('client_image1', models.ImageField(null=True, upload_to='user_images/')),
                ('client_image2', models.ImageField(null=True, upload_to='user_images/')),
                ('client_image3', models.ImageField(null=True, upload_to='user_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_razonsocial', models.TextField(max_length=250, null=True)),
                ('participacion', models.IntegerField(null=True)),
                ('identification', models.CharField(max_length=250, null=True)),
                ('number', models.IntegerField(null=True)),
                ('ciudad', models.CharField(max_length=250, null=True)),
                ('direccion', models.CharField(max_length=250, null=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WizardForm')),
            ],
        ),
    ]
