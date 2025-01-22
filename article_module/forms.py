from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'checkout__input',
            'placeholder': 'Leave a comment...',
            'rows': 4,  # تعداد خطوط پیش‌فرض
        }),
        label='message',
        max_length=500,
    )
