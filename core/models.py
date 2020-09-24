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


# class PhoneOTP(models.Model):
#     # phone_regex = RegexValidator(regex=r'^\+?234?\d(9,14)$',
#     #     message="Phone number must be entered in format of +2348044234244 up to 14 digits")
#     # phone = models.CharField(validator=[phone_regex], max_length=15, unique=True)
#     phone = models.CharField(max_length=15, unique=True)
#     otp = models.CharField(max_length=6)
#     initial = models.IntegerField(blank=True, null=True)
#     last = models.IntegerField(blank=True, null=True)
#     validated = models.BooleanField(default=False)
#     count = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return f'{self.phone_number} is sent {self.otp}'


# def add_timer(sender, instance, *args, **kwargs):
#     instance.initial = int(time.time())
#     instance.last = instance.initial + 30


# pre_save.connect(add_timer, sender=PhoneOTP)


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


# class Step1FormModel(models.Model):

#     # client_id = models.ForeignKey(Client,on_delete=models.CASCADE)
#     id = models.UUIDField(
#         primary_key=True, null=False, unique=True, default=uuid.uuid4, editable=False)
#     personal_id = models.TextField(max_length=250, null=True)
#     firstname = models.CharField(max_length=250, null=True)
#     lastname = models.CharField(max_length=250, null=True)
#     bemovil_id = models.IntegerField(null=True)
#     expedition_date = models.DateField(null=True)
#     expedition_place = models.CharField(max_length=250, null=True)
#     mobile_phone = models.IntegerField(null=True)
#     number = models.IntegerField(null=True)
#     email = models.EmailField(max_length=255, null=True)

#     address = models.TextField(max_length=250, null=True)
#     city = models.CharField(max_length=250, null=True)
#     valley = models.CharField(max_length=250, null=True)


#     def __str__(self):
#         return str(self.firstname)


# class Step2FormModel(models.Model):
#     # client_id = models.OneToOneField(
#     #     Step1FormModel, null=True, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=250, null=True)
#     actividad_economica=models.CharField(max_length=250, null=True)
#     direccion = models.TextField(max_length=250, null=True)
#     barrio = models.CharField(max_length=250, null=True)
#     ciudad = models.CharField(max_length=250, null=True)
#     departamento = models.CharField(max_length=250, null=True)
#     mobile_phone =models.IntegerField(blank=True, null=True)
#     telefono_fijo =models.IntegerField(blank=True, null=True)
#     email =models.EmailField(blank=True, null=True)
#     ingresos =models.IntegerField(blank=True, null=True)
#     total_activos =models.IntegerField(blank=True, null=True)
#     egresos =models.IntegerField(blank=True, null=True)
#     total_pasivos = models.IntegerField(blank=True, null=True)
#     name_razonsocial = models.TextField(max_length=250, null=True)
#     participacion = models.IntegerField(max_length=250, null=True)
#     identification = models.CharField(max_length=250, null=True)
#     number =models.IntegerField(max_length=250, null=True)
#     address =models.CharField(max_length=250, null=True)
#     city =models.CharField(max_length=250, null=True)


# class Step3FormModel(models.Model):
#     # client_id = models.OneToOneField(
#     terms=models.c


# class UserPictures(models.Model):
#     '''
#     Model to manage multiple pictures of the user
#     '''
#     #user_uuid = models.UUIDField(null=True)
#     # client_id = models.OneToOneField(
#     #     Step1FormModel, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     image1 = models.ImageField(upload_to='user_images/', null=True)
#     image2 = models.ImageField(upload_to='user_images/', null=True)
#     image3 = models.ImageField(upload_to='user_images/', null=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.name)


# class FileModel(models.Model):
#     # client_id = models.one(
#     #     Step1FormModel, null=True, on_delete=models.CASCADE)
#     uploader = models.CharField(max_length=20)
#     firstFile = models.FileField(upload_to='documents')
#     secondFile = models.FileField(upload_to='documents')
#     file = models.BinaryField(null=True, blank=False)

#     def __str__(self):
#         return self.uploader
