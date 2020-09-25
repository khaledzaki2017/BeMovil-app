from django.db import models
from django.db.models.signals import pre_save
import time
import uuid

from multiselectfield import MultiSelectField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from sortedone2many.fields import SortedOneToManyField
from multiselectfield import MultiSelectField

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# Create your models here.

# class Client(models.Model):
#     bemovil_id = models.IntegerField(null=True, primary_key=True)
#     email = models.EmailField(max_length=255, null=True)
#     mobile_phone = models.IntegerField(null=True)


#     def __str__(self):
#         return str(self.email)


TYPE_CHOICES = ((1, 'Natural'),
                (2, 'Juridica'))


class WizardForm(models.Model):

    # id = models.UUIDField(
    #     primary_key=True, null=False, unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        primary_key=True, null=False, unique=True, default="")
    _type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    personal_id = models.TextField(max_length=250, null=True)
    firstname = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)
    bemovil_id = models.IntegerField(null=True)
    expedition_date = models.DateField(null=True)
    expedition_place = models.CharField(max_length=250, null=True)
    mobile_phone = models.IntegerField(null=True)
    number = models.IntegerField(null=True)

    address = models.TextField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    valley = models.CharField(max_length=250, null=True)

    company_name = models.CharField(max_length=250, null=True)
    actividad_economica = models.CharField(max_length=250, null=True)
    direccion = models.TextField(max_length=250, null=True)
    barrio = models.CharField(max_length=250, null=True)
    ciudad = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    mobile_phone_fin = models.IntegerField(null=True)
    email_fin = models.EmailField(null=True, unique=True, default="")

    telefono_fijo = models.IntegerField(blank=True, null=True)
    ingresos = models.IntegerField(blank=True, null=True)
    total_activos = models.IntegerField(blank=True, null=True)
    egresos = models.IntegerField(blank=True, null=True)
    total_pasivos = models.IntegerField(blank=True, null=True)

    uploader = models.CharField(max_length=250, null=True)
    firstFile = models.FileField(upload_to='documents')
    secondFile = models.FileField(upload_to='documents')
    file = models.BinaryField(null=True, blank=False)

    name_info = models.CharField(max_length=250, null=True)
    email_info = models.EmailField(null=True, unique=True, default="")
    lastname_info = models.CharField(max_length=250, null=True)
    number_info = models.IntegerField(null=True)

    id_image1 = models.ImageField(upload_to='user_images/id_images', null=True)
    id_image2 = models.ImageField(upload_to='user_images/id_images', null=True)

    client_image1 = models.ImageField(upload_to='user_images/', null=True)
    client_image2 = models.ImageField(upload_to='user_images/', null=True)
    client_image3 = models.ImageField(upload_to='user_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'This is {self.firstname} {self.lastname} Form'


class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.Mobile)


class Partner(models.Model):
    main = models.ForeignKey(WizardForm, on_delete=models.CASCADE)
    name_razonsocial = models.TextField(max_length=250, null=True)
    participacion = models.IntegerField(null=True)
    identification = models.CharField(max_length=250, null=True)
    number = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f'{self.name_razonsocial} is partner to {self.main}'
