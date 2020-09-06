from django.db import models

# Create your models here.


class Step1FormModel(models.Model):
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    bemovil_id = models.IntegerField(null=True)
    personal_id = models.TextField(max_length=100, null=True)
    expedition_date = models.DateField(null=True)
    expedition_place = models.CharField(max_length=100, null=True)
    mobile_phone = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    address = models.TextField(max_length=100, null=True)
    email = models.EmailField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    valley = models.CharField(max_length=100, null=True)


class Step2FormModel(models.Model):
    address = models.TextField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    valley = models.CharField(max_length=100, null=True)


class Step3FormModel(models.Model):
    mobile_phone = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


class UserPictures(models.Model):
    '''
    Model to manage multiple pictures of the user
    '''
    #user_uuid = models.UUIDField(null=True)
    name = models.CharField(max_length=200, null=True)
    image1 = models.ImageField(upload_to='user_images/', null=True)
    image2 = models.ImageField(upload_to='user_images/', null=True)
    image3 = models.ImageField(upload_to='user_images/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
