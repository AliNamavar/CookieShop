from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'checkout__input__add', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'checkout__input__add', 'placeholder': 'Last Name'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'checkout__input__add', 'placeholder': 'Street Address'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'checkout__input'})
    )
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'checkout__input'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'checkout__input'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if len(password) < 8:
            self.add_error('email', "رمز عبور باید حداقل ۸ کاراکتر باشد")

        if not any(char.isdigit() for char in password):
            self.add_error('email', "رمز عبور باید شامل حداقل یک عدد باشد")

        if not any(char.isupper() for char in password):
            self.add_error('email', "رمز عبور باید شامل حداقل یک حرف بزرگ باشد")

        if not any(char in "!@#$%^&*()_+" for char in password):
            self.add_error('email', "رمز عبور باید شامل حداقل یک کاراکتر ویژه (!@#$%^&*()_+) باشد")

        if password != repeat_password:
             self.add_error('email', "رمز عبور و تکرار آن مطابقت ندارند")


        return cleaned_data


class ActivationCodeForm(forms.Form):
    activation_code = forms.CharField(
        max_length=72,
        widget=forms.TextInput(attrs={
            'class': 'checkout__input__add',
            'placeholder': 'Activation Code'
        })
    )




class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'checkout__input'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'checkout__input', 'placeholder': 'Password'}))

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Your Email'
        })
    )


class ResetPasswordForm(forms.Form):
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'checkout__input'})
    )
    RepeatPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'checkout__input'})
    )
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("Password")
        repeat_password = cleaned_data.get("RepeatPassword")
        if password != repeat_password:
            self.add_error('Password', "Passwords don't match")

        return cleaned_data