from django.db import models
from django.contrib.auth.models import  User
# Create your models here.

class UserProfile(models.Model):
    #instead of creating a new user type derived from the Django user
    #use the existng class and add some fields
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional fields for knotical purpose
    company_name = models.CharField(max_length=256, blank=True)
    company_url = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
