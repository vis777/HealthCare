from django.db import models


class Chat_Intraction(models.Model):
    type=models.CharField(max_length=20)

# Create your models here.
class ExpertDb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    Post = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True)
    UserNaMe = models.CharField(max_length=100, null=True, blank=True)
    PassWoRd = models.CharField(max_length=100, null=True, blank=True)
    is_blocked = models.BooleanField(default=False)
    CI_ID=models.ForeignKey(Chat_Intraction,on_delete=models.CASCADE,null=True)

class DiseaseDb(models.Model):
    DName = models.CharField(max_length=100, null=True, blank=True)

class DatasetDB(models.Model):
    Question = models.CharField(max_length=100, null=True, blank=True)
    Answer = models.CharField(max_length=100, null=True, blank=True)
class HomeremedyDb(models.Model):
    DName = models.CharField(max_length=100, null=True, blank=True)
    HName = models.CharField(max_length=100, null=True, blank=True)
    Remedy = models.CharField(max_length=100, null=True, blank=True)

