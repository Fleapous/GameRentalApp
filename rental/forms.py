from django import forms

from identity.models import Address
from .models import Rental
from django.contrib.auth.models import User


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['game', 'return_date', 'address']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game'].widget = forms.HiddenInput()
        user = self.initial.get('user')
        self.fields['address'].queryset = Address.objects.filter(user=user)
