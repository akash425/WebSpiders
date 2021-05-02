
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings

import random

from .models import UserOTP


# Login view
class ViewLogIn(LoginView):
    template_name = 'accounts/login/LogIn.html'
    fields = "__all__"
    redirect_authenticated_user = True

    # Redirecting to home page
    def get_success_url(self):
        return reverse_lazy('sign_up')  # for test, should contain home url

    # Redirecting logged in users to home page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render('home')
        return super(ViewLogIn, self).get(*args, **kwargs)


# Create sign up form

class CreateSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Display Sign up page
def sign_up(request):
    form = CreateSignUpForm()
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Username'
    })
    form.fields['email'].widget.attrs.update({
        'placeholder': 'Email'
    })
    form.fields['password1'].widget.attrs.update({
        'placeholder': 'Password'
    })
    form.fields['password2'].widget.attrs.update({
        'placeholder': 'Confirm Password'
    })
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(email=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                messages.success(request, f'Account is Created For {usr.username}')
                return redirect('login')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'accounts/signup/SignUp.html', {'otp': True, 'usr': usr})

        form = CreateSignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            usr = User.objects.get(email=email)
            usr.email = email
            usr.name = username

            usr.is_active = False
            usr.save()
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)

            mess = f"Hello {usr.name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome - Please Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )

            return render(request, 'accounts/signup/SignUp.html', {'otp': True, 'usr': usr})

            # messages.success(request, 'Account was successfully created for '+ user)
            # return redirect('login')

    else:
        form = CreateSignUpForm(request.POST)
    return render(request, 'accounts/signup/SignUp.html', {'form': form})
    # context = {'form': form}
    # return render(request, 'accounts/signup/SignUp.html', context)


def resend_otp(request):
    if request.method == "GET":
        get_usr = request.GET['usr']
        if User.objects.filter(username=get_usr).exists() and not User.objects.get(username=get_usr).is_active:
            usr = User.objects.get(username=get_usr)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {usr.name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to ITScorer - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return HttpResponse("Resend")

    return HttpResponse("Can not Send OTP")
