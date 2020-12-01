from django import forms
from django.contrib.auth.models import User

#import the user profile model
from usermanagement.models import UserProfile

class UserForm(forms.ModelForm):
    #create a form for original user class
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    #create a form for the additional fields
    class Meta():
        model = UserProfile
        fields = ('company_name','company_url')
