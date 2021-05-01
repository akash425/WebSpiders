from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User


# Login view
class ViewLogIn(LoginView):
    template_name = 'accounts/login/LogIn.html'
    fields = "__all__"
    redirect_authenticated_user = True

    # Redirecting to home page
    def get_success_url(self):
        return reverse_lazy('base.html')  # for test, should contain home url


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
        form = CreateSignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/signup/SignUp.html', context)
