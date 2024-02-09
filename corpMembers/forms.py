from django import forms
from .models import User, Contact
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserForm(UserCreationForm):
  
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'status', 'discipline', 'image', 'phone_number', 'email', 'PPA', 'category', 'gender']



        labels = {
            'password1':'Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Short Username for FrontPage'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'discipline': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'PPA': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

    
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = User  # Specify the User model
        fields = ('username', 'password')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'comment']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}),
        'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
        'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5,'placeholder':'Comment'}),
    }
        

