from django import forms
from .models import feedback_Model

from django import forms
from .models import feedback_Model


class feedbackForm(forms.Form):
    # feedback = forms.Textarea(
    #     attrs={'class': 'checkout__input'}
    #
    # )
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'checkout__input', 'placeholder': 'Password'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'checkout__input', 'placeholder': 'Text'}))

    rating = forms.ChoiceField(choices=[(i, f'{i} Star') for i in range(1, 6)],
                               widget=forms.Select(attrs={'class': 'checkout__input', 'placeholder': 'Rating'}))
