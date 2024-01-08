from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from Backend.models import ExpertDb,Chat_Intraction
User = get_user_model()
# Create your models here.
class SymptomDb(models.Model):
    DName = models.CharField(max_length=100, null=True, blank=True)
    Symptom = models.CharField(max_length=100, null=True, blank=True)

class LoginDb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    UserName = models.CharField(max_length=100, null=True, blank=True)
    PassWord = models.CharField(max_length=100, null=True, blank=True)
    CI_ID=models.ForeignKey(Chat_Intraction,on_delete=models.CASCADE,null=True)



class SuggestionDb(models.Model):
    Login_ID = models.ForeignKey(LoginDb, on_delete=models.CASCADE, null=True)
    Ex_Id = models.ForeignKey(ExpertDb, on_delete=models.CASCADE,null=True)
    Suggestion = models.CharField(max_length=100, null=True, blank=True)
    Discription = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateField(auto_now_add=True)


class ComplainDb(models.Model):
    Login=models.ForeignKey(LoginDb,on_delete=models.CASCADE,null=True)
    Complaint = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateField(auto_now_add=True)
    Reply = models.CharField(max_length=100, null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    login_db = models.OneToOneField(LoginDb, on_delete=models.CASCADE)
    is_expert = models.BooleanField(default=False)


class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs
class Thread(models.Model):
    first_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


class ChatMessage(models.Model):
    fromid = models.ForeignKey(Chat_Intraction, null=True, blank=True, on_delete=models.CASCADE, related_name='fromid')
    toid = models.ForeignKey(Chat_Intraction, null=True, blank=True, on_delete=models.CASCADE, related_name='toid')

    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ChatBotUser(models.Model):
    fromid = models.ForeignKey(LoginDb, null=True, blank=True, on_delete=models.CASCADE, related_name='fromid')

    message = models.TextField()
    reply = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)