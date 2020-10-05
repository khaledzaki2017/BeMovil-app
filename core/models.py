from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
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


# TYPE_CHOICES = ((1, 'Natural'),
#                 (2, 'Juridica'))


class WizardFormNatural(models.Model):
    # ****************************step1************************************
    id = models.UUIDField(
        primary_key=True, null=False, unique=True, default=uuid.uuid4, editable=False)
    # email = models.EmailField(
    #     primary_key=True, null=False, default="")
    email = models.EmailField(null=True, default="")
    _type = models.CharField(max_length=100,  null=True)
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
    # ****************************step2************************************

    company_name = models.CharField(max_length=250, null=True)
    actividad_economica = models.CharField(max_length=250, null=True)
    direccion = models.TextField(max_length=250, null=True)
    barrio = models.CharField(max_length=250, null=True)
    ciudad = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    mobile_phone_fin = models.IntegerField(null=True)
    email_fin = models.EmailField(null=True, default="")

    telefono_fijo = models.IntegerField(blank=True, null=True)
    ingresos = models.IntegerField(blank=True, null=True)
    total_activos = models.IntegerField(blank=True, null=True)
    egresos = models.IntegerField(blank=True, null=True)
    total_pasivos = models.IntegerField(blank=True, null=True)
    # ****************************step4************************************

    uploader = models.CharField(max_length=250, null=True, default="")
    firstFile = models.FileField(upload_to='documents', default="")
    secondFile = models.FileField(upload_to='documents', default="")
    # ****************************step5************************************

    name_info = models.CharField(max_length=250, null=True)
    email_info = models.EmailField(null=True, default="")
    lastname_info = models.CharField(max_length=250, null=True)
    number_info = models.IntegerField(null=True)

    id_image1 = models.ImageField(upload_to='user_images/id_images', null=True)
    id_image2 = models.ImageField(upload_to='user_images/id_images', null=True)

    client_image1 = models.ImageField(upload_to='user_images/', null=True)
    client_image2 = models.ImageField(upload_to='user_images/', null=True)
    client_image3 = models.ImageField(upload_to='user_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False)
    # Razon_social = models.CharField(max_length=250, null=True)
    # nit = models.CharField(max_length=250, null=True)
    # home_address = models.CharField(max_length=250, null=True)
    # question1 = models.BooleanField(default=False)
    # question2 = models.BooleanField(default=False)


def __str__(self):
    return f'This is {self.firstname} {self.lastname} Form'


class WizardFormJuridica(models.Model):
    # ****************************step1************************************
    id = models.UUIDField(
        primary_key=True, null=False, unique=True, default=uuid.uuid4, editable=False)
    # email = models.EmailField(
    #     primary_key=True, null=False, default="")
    email = models.EmailField(null=True, default="")
    _type = models.CharField(max_length=100,  null=True)
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
    # ****************************step2************************************

    company_name = models.CharField(max_length=250, null=True)
    actividad_economica = models.CharField(max_length=250, null=True)
    direccion = models.TextField(max_length=250, null=True)
    barrio = models.CharField(max_length=250, null=True)
    ciudad = models.CharField(max_length=250, null=True)
    departamento = models.CharField(max_length=250, null=True)
    mobile_phone_fin = models.IntegerField(null=True)
    email_fin = models.EmailField(null=True, default="")

    telefono_fijo = models.IntegerField(blank=True, null=True)
    ingresos = models.IntegerField(blank=True, null=True)
    total_activos = models.IntegerField(blank=True, null=True)
    egresos = models.IntegerField(blank=True, null=True)
    total_pasivos = models.IntegerField(blank=True, null=True)
    # ****************************step4************************************

    uploader = models.CharField(max_length=250, null=True, default="")
    firstFile = models.FileField(upload_to='documents', default="")
    secondFile = models.FileField(upload_to='documents', default="")
    # ****************************step5************************************

    name_info = models.CharField(max_length=250, null=True)
    email_info = models.EmailField(null=True, default="")
    lastname_info = models.CharField(max_length=250, null=True)
    number_info = models.IntegerField(null=True)

    id_image1 = models.ImageField(upload_to='user_images/id_images', null=True)
    id_image2 = models.ImageField(upload_to='user_images/id_images', null=True)

    client_image1 = models.ImageField(upload_to='user_images/', null=True)
    client_image2 = models.ImageField(upload_to='user_images/', null=True)
    client_image3 = models.ImageField(upload_to='user_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False)
    Razon_social = models.CharField(max_length=250, null=True)
    nit = models.CharField(max_length=250, null=True)
    home_address = models.CharField(max_length=250, null=True)
    question1 = models.BooleanField(default=False)
    question2 = models.BooleanField(default=False)


def __str__(self):
    return f'This is {self.firstname} {self.lastname} Form'


class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.Mobile)


class Partner(models.Model):
    main = models.ForeignKey(WizardFormJuridica, on_delete=models.CASCADE)
    name_razonsocial = models.TextField(max_length=250, null=True)
    participacion = models.IntegerField(null=True)
    identification = models.CharField(max_length=250, null=True)
    number = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=250, null=True)
    direccion = models.CharField(max_length=250, null=True)

    def __str__(self):
        return f'{self.name_razonsocial} is partner to {self.main}'


# ****************** ADMIN PANEL MODELS **************************

class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # title = models.CharField(max_length=5)
    # dob = models.DateField()
    # photo = models.ImageField(upload_to='uploads', blank=True)


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=True)
    firstname = models.CharField(null=True, max_length=100)
    url = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
