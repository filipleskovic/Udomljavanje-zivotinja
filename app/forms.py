from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from app.models import User,Animal,AnimalType
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput


class CustomUserForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DatePickerInput())
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    avatar_url = forms.CharField(max_length=128, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','oib','address','city', 'date_of_birth',
                  'gender', 'avatar_url', 'email','password1', 'password2']
    widgets = {
            'date_of_birth': DateTimePickerInput(),  
            }   
        
class AnimalForm(ModelForm):
    GENDER_CHOICES = [
        ('muško', 'Muško'),
        ('žensko', 'Žensko'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    avatar_url = forms.CharField(max_length=128, required=True)
        
    class Meta:
        model = Animal
        fields = ['name', 'age', 'description', 'type',
                  'height', 'weight','gender','avatar_url']
        
class AnimalTypeForm(ModelForm):
    ANIMAl_CHOICES=[
        ('CAT', 'CAT'),
        ('DOG', 'DOG'),
    ]
    type=forms.ChoiceField(choices=ANIMAl_CHOICES,required=True)
    class Meta:
        model=AnimalType
        fields =['lifespan','type','breed']