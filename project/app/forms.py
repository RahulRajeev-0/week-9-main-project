from django import forms
from django.contrib.auth.models import User

class User_form(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'username',
            # 'first_name',
            # 'last_name',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
        ]

        widgets={
            'username':forms.TextInput,
            # 'first_name':forms.TextInput,
            # 'last_name':forms.TextInput,
            'email':forms.EmailInput,
            'is_active':forms.CheckboxInput,
            'is_staff':forms.CheckboxInput,
            'is_superuser':forms.CheckboxInput,

        }

