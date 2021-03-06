from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from .models import Resume
from django.conf import settings
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail



# Create your views here.
# def home(request):
#     return HttpResponse('resume form')



def get_resume(request):
    user_data=User.objects.filter(username=request.user.get_username())
    #user_data=User.objects.all()
    
    print(request.user.get_username())
    
    return render(request, "resume/resume_form.html", {'user_data':user_data})
    

class IndexView(generic.ListView):
    context_object_name = 'resume_list'
    template_name = 'resume/list.html'
    
    def get_queryset(self):
        print(self.request.user)
        return Resume.objects.filter(user=self.request.user)
    
class AddResume(CreateView):
    model = Resume
    def resume_mail(self):
        
        mess = f"Hello Admin,\nPlease Approve {self.request.user}'s Resume \nThanks!"

        send_mail(
            "Resume Approval Request",
            mess,
            settings.EMAIL_HOST_USER,
            ['akashkushwaha425@gmail.com'],
            fail_silently=False
        )

    
    fields = ['first_name','last_name','image','address','EduLevel','CourseName', 'StartingYear','IsAppearing','PassOutYear','skills','dob', 'user']
    
    
    
class UpdateResume(UpdateView):
    model = Resume
    fields = ['first_name','last_name','image','address','EduLevel','CourseName', 'StartingYear','IsAppearing','PassOutYear','skills','dob', 'user']
    
    
class DeleteResume(DeleteView):
    model = Resume
    
    success_url = reverse_lazy('resume:index')    