
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'resume'

urlpatterns = [
    path('resume/', views.get_resume, name='get_resume'),
    
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^resume/create/$',views.AddResume.as_view(),name='create_resume'),

    url(r'^resume/(?P<pk>[0-9]+)/$', views.UpdateResume.as_view(), name='resume-update'),
 
     #modelforms/product/(?P<pk>[0-9]+)/delete
    url(r'^resume/(?P<pk>[0-9]+)/delete$', views.DeleteResume.as_view(), name='resume-delete'),    

    
]

