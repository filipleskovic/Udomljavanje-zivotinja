from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from app.models import User,Animal,AnimalType
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput


class CustomUserForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=DatePickerInput(),label='Datum rođenja')
    GENDER_CHOICES = [
        ('male', 'Muško'),
        ('female', 'Žensko'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True,label='Spol')
    avatar_url = forms.CharField(max_length=128, required=True,label='URL Slike')
    widgets = {
            'date_of_birth': DateTimePickerInput(),  
            }   
    password1 = forms.CharField(
        label='Zaporka',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Potvrda zaporke',
        widget=forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name','oib','address','city', 'date_of_birth',
                  'gender', 'avatar_url', 'email','password1','password2']
        labels={
            'first_name':'Ime',
            'last_name':'Prezime',
            'address':'Adresa',
            'city':'Grad',
            'email':'Adresa e-pošte',
        }
    
       
class AnimalForm(ModelForm):
    GENDER_CHOICES = [
        ('muško', 'Muško'),
        ('žensko', 'Žensko'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True,label='Spol')
    avatar_url = forms.CharField(max_length=128, required=True,label='URL Slike')
    class Meta:
        model = Animal
        fields = ['name', 'age', 'description', 'type',
                  'height', 'weight','gender','avatar_url']
        labels = {
            'name': 'Ime',
            'age': 'Dob',
            'description': 'Opis',
            'type': 'Vrsta',
            'height': 'Visina',
            'weight': 'Težina',
        }
        
class AnimalTypeForm(ModelForm):
    ANIMAl_CHOICES=[
        ('DOG','Pas'),
        ('CAT', 'Mačka'),
    ]
    type=forms.ChoiceField(choices=ANIMAl_CHOICES,required=True,label='Životinja')
    class Meta:
        model=AnimalType
        fields =['lifespan','type','breed']
        labels={
            'lifespan':'Životni vijek',
            'breed':'Pasmina'
        }
        
        
        
            