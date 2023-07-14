from django import forms
from myapp.models import Movies
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')