from django.shortcuts import render
from django.http import HttpResponse

from .models import SignUp

# Display Sign up page

def sign_up(request):
    return render(request, 'accounts\signup\SignUp.html')



