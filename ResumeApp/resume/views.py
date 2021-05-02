from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls.base import reverse_lazy
from . import forms
from .models import Resume

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from ResumeApp import resume

# Create your views here.
'''
def home(request):
    return HttpResponse('resume form')

def get_resume(request):
    resume_data = forms.resume_form
    return render(request, "resume/res_form.html", {'form':resume_data})
    '''

class IndexView(generic.ListView):
    context_object_name = 'resume_list'
    template_name = 'resume/list.html'
    def get_queryset(self):
        return Resume.objects.all()
    
class AddResume(CreateView):
    model = Resume
    fields = ['first_name', 'last_name', 'address']
    
    
class UpdateResume(CreateView):
    model = Resume
    fields = ['first_name', 'last_name', 'address']
    
    
class DeleteResume(DeleteView):
    model = Resume
    
    success_url = reverse_lazy('resume/list.html')    

