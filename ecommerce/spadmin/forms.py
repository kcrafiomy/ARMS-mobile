from django import forms
from userside.models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'
