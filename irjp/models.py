from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Registration(models.Model):
    sname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    nostreet = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    telno = models.CharField(max_length=100)
    birthday = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    civilstatus = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    rescertno = models.CharField(max_length=100)
    issued = models.CharField(max_length=100)
    at = models.CharField(max_length=100)
    SSSno = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)
    talent = models.CharField(max_length=100)
    physical = models.CharField(max_length=100)
    married = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    fatherN = models.CharField(max_length=100)
    occupationF = models.CharField(max_length=100)
    mobileF = models.CharField(max_length=100)
    addressF = models.CharField(max_length=100)
    motherN = models.CharField(max_length=100)
    occupationM = models.CharField(max_length=100)
    mobileM = models.CharField(max_length=100)
    addressM = models.CharField(max_length=100)
    brothers = models.CharField(max_length=100)
    sister = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


