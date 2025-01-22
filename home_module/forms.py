from django import forms
from .models import feedback_Model

from django import forms
from .models import feedback_Model


class feedbackForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Text'}))

    rating = forms.ChoiceField(choices=[(i, f'{i} Star') for i in range(1, 6)],
                               widget=forms.Select(attrs={'class': 'checkout__input', 'placeholder': 'Rating'}))

class check_address(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'checkout__input__add', 'placeholder': 'Street Address'})
    )