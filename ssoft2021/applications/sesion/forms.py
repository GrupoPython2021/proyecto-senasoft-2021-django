from django import forms

#import models
from .models import Sesion
from applications.users.models import User


class CreateSalaViewForm(forms.Form):
    """Form para CreateSalaViewForm"""

    class Meta:
        model = Sesion
        fields = 'sesion'

