import uuid

from django.db import models


# Create your models here.

class Address(models.Model):
    address_line_1 = models.CharField(max_length=200, null=True, blank=True)
    address_line_2 = models.CharField(max_length=200, null=True, blank=True)
    pin_code = models.CharField(max_length=20)
    town = models.CharField(max_length=300)
    taluka = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    longitude = models.FloatField(default=0.0, null=True, blank=True)
    lattitude = models.FloatField(default=0.0, null=True, blank=True)


class BloodGroups(models.Model):
    group = models.CharField(max_length=56)


class UserType(models.Model):
    type = models.CharField(max_length=200)


class UserInfo(models.Model):
    blood_group = models.ForeignKey(BloodGroups, null=True)
    wbc = models.IntegerField(null=True)
    prc = models.IntegerField(null=True)
    plc = models.IntegerField(null=True)
    prp = models.IntegerField(null=True)
    ffp = models.IntegerField(null=True)


class UserLogin(models.Model):
    user = models.ForeignKey(User, null=True, default=None)
    token = models.UUIDField(default=uuid.uuid4, editable=False, null=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    user_name = models.EmailField(null=False, blank=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_type = models.ForeignKey(UserType, null=True, default=None)
    phone_number = models.IntegerField()
    address = models.ForeignKey(Address, null=True)
    enable = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)


class BloodRequest(models.Model):
    full_name = models.CharField(max_length=256)
