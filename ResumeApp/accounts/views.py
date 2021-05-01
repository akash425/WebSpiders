from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


# Login view
class ViewLogIn(LoginView):
    template_name = 'accounts/login/LogIn.html'
    fields = "__all__"
    redirect_authenticated_user = True

    # Redirecting to home page
    def get_success_url(self):
        return reverse_lazy('base.html')  # for test, should contain home url

    # Redirecting logged in users to home page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return render('base.html')
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
        form = CreateSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for '+ user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/signup/SignUp.html', context)
