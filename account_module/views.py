from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, ActivationCodeForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from utils.email_service import send_email
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class RegisterView(View):

    def get(self, request):
        context = {
            'form': RegisterForm()
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_first_name = form.cleaned_data.get('first_name')
            user_last_name = form.cleaned_data.get('last_name')
            user_address = form.cleaned_data.get('address')
            user_password = form.cleaned_data.get('password')
            user_email = form.cleaned_data.get('email')

            user = User.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error(field='email', error='Email already registered.')
                return render(request, 'account_module/register.html', context={
                    'form': form
                })
            else:
                new_user = User(
                    email=user_email,
                    first_name=user_first_name,
                    last_name=user_last_name,
                    address=user_address,
                    email_active_code=get_random_string(8),
                    is_active=False,
                    username=user_first_name + user_last_name
                )
                new_user.set_password(user_password)
                new_user.save()
                send_email(
                    subject='email active code',
                    to=user_email,
                    context={'form': form,
                             'user': new_user},
                    template_name='send_mails/active_email_send.html'
                )
                messages.success(request, 'کد تأیید به ایمیل شما ارسال شد')
                return redirect(reverse('email_verification'))

        return render(request, 'account_module/register.html', context={
            'form': form
        })


class email_verification(View):
    def get(self, request):
        form = ActivationCodeForm()
        context = {
            'form': form
        }
        return render(request, 'account_module/code-activate.html', context)

    def post(self, request):
        form = ActivationCodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['activation_code']
            user = User.objects.filter(email_active_code__iexact=code).first()
            if user is not None:
                user.is_active = True
                user.email_active_code = get_random_string(8)
                user.save()
                login(request, user)
                messages.success(request, 'اکانت شما فعال شد')
                return redirect(reverse('home'))
            else:
                form.add_error('activation_code', 'کد نامعتبر است')
                return render(request, 'account_module/code-activate.html', context={
                    'form': form
                })
        return render(request, 'account_module/code-activate.html', context={
            'form': form
        })


class logoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت خارج شدید')
        return redirect(reverse('login'))


class LoginView(View):
    def get(self, request):
        return render(request, 'account_module/login.html', context={
            'form': LoginForm()
        });

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_password = form.cleaned_data['password']
            user = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if user.is_active:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        messages.success(request, 'لاگ این با موفقیت انجام شد')
                        return redirect(reverse('home'))
                    else:
                        form.add_error('email', 'کاربر یافت نشد')
                else:
                    form.add_error('email', 'اکانت شما فعال نیست')
                    send_email(
                        subject='email active code',
                        to=user_email,
                        context={'form': form,
                                 'user': user},
                        template_name='send_mails/active_email_send.html'
                    )
                    messages.success(request, 'اکانت شما فعال نست لطفا اول اکانت خود را فعال کنید کد فعالسازی به ایمیل شما ارسال شد')
                    return redirect('email_verification')
            else:
                form.add_error('email', 'ایمیل وارد شده صحیح نیست')
                return render(request, 'account_module/login.html', context={
                    'form': form
                })
        return render(request, 'account_module/login.html', context={
            'form': form
        })

# class ForgotPassView(View):
#     def get(self, request):
#         context = {
#             'form': ForgotPasswordForm()
#         }
#         return render(request, 'account_module/forgotPass.html', context)
#
#     def post(self, request):
#         form = ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             user:User = User.objects.filter(email__iexact=email).first()
#             if user is None:
#                 form.add_error('email', 'ایمیل وارد شده صحیح نمی باشد')
#                 return render(request, 'account_module/forgotPass.html', context={
#                     'form': form
#                 })
#             send_email(
#                 to=email,
#                 subject='Reset your password',
#                 context={'form': form,'user': user},
#                 template_name='send_mails/forgot_password_send.html'
#
#             )
#
#             messages.success(request, 'کد تایید به ایمل شما ارسال شد ایمیل خود را چک کنید')
#             return redirect(reverse('home'))
#
#         return render(request, 'account_module/forgotPass.html', context={
#             'form': form,
#         })

class ForgotPassView(SuccessMessageMixin, FormView):
    template_name = 'account_module/forgotPass.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('home')
    success_message = 'reset password link send to your email'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email__iexact=email).first()
        if not user:
            form.add_error('email', 'ایمیل وارد شده صحیح نمی‌باشد')
            return self.form_invalid(form)


        send_email(
            to=email,
            subject='Reset your password',
            context={'form': form, 'user': user},
            template_name='send_mails/forgot_password_send.html'
        )
        return super().form_valid(form)


def ChangePass(request, email_active_code):
    user = get_object_or_404(User, email_active_code=email_active_code)


    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_pass = form.cleaned_data['Password']
            user.password = make_password(new_pass)
            user.email_active_code = get_random_string(8)
            user.save()
            messages.success(request, 'pass شما با موفقیت تغییر کرد ')
            return redirect(reverse('login'))
        return render(request, 'account_module/ChangePass.html', context={
            'form': form
        })
    else:
        context = {
            'form': ResetPasswordForm(),
        }
        return render(request, 'account_module/ChangePass.html', context)

