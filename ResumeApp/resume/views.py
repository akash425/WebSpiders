from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from .models import Resume

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from ResumeApp import resume

# Create your views here.
# def home(request):
#     return HttpResponse('resume form')

def get_resume(request):
    user_data=User.objects.filter(username=request.user)
    print(user_data)
    
    return render(request, "resume/resume_form.html", {'user_data':user_data})
    

class IndexView(generic.ListView):
    context_object_name = 'resume_list'
    template_name = 'resume/list.html'
    def get_queryset(self):
        return Resume.objects.all()
    
class AddResume(CreateView):
    model = Resume
    fields = ['__all__']
    
    
class UpdateResume(CreateView):
    model = Resume
    fields = ['first_name', 'last_name', 'address']
    
    
class DeleteResume(DeleteView):
    model = Resume
    
    success_url = reverse_lazy('resume/list.html')    

