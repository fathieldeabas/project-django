from django import forms
from .models import Myuser
class Loginform(forms.ModelForm):
    class Meta:
        model=Myuser
        fields=['Username','Password']