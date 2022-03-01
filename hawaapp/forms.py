from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import HawaUser


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(UserCreationForm):
    class Meta:
        model = HawaUser

        fields = ['email', 'firstname', 'lastname',
                  'password1', 'password2', 'birthdate']
        widgets = {
            'birthdate': DateInput()
        }
