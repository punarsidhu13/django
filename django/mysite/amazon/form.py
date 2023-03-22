from django import forms
from .models import Amazon
from django.contrib.auth.models import User

class AmazonForm(forms.ModelForm):
    class Meta:
        model = Amazon
        fields = '__all__'


class CreateNewUserForm(forms.ModelForm):
      class Meta:
            model = User
            fields = ('username','password','email')        