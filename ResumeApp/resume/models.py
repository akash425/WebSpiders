from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# class Qualifications(models.Model):
#     EduLevel = models.CharField(max_length=100)
#     CourseName  = models.CharField(max_length=100)
#     StartingYear = models.DateField()
#     IsAppearing = models.BooleanField()
#     PassOutYear = models.DateField()

    

# class Skills_data(models.Model):
#    ratings=(
#     ("1", 1),
#     ("2", 2),
#     ("3", 3),
#     ("4", 4),
#     ("5", 5),
# )
#    SkillName = models.CharField(max_length=100)
#    Rating = models.CharField(choices=ratings, max_length=10)
    
    
    
    
class Resume(models.Model):
    
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='blog/blogimages')
    address =  models.TextField()
    dob = models.DateField(null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    EduLevel = models.CharField(max_length=100, null=True)
    CourseName  = models.CharField(max_length=100,default='MCA')
    StartingYear = models.DateField(null = True)
    IsAppearing = models.BooleanField(default=False)
    PassOutYear = models.DateField(null = True)
    skills = models.CharField(max_length=200, null = True)
    status = models.BooleanField(default=False)
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # skill_user = models.ForeignKey(Skills_data, on_delete=models.CASCADE)
    # qualifiction_user = models.ForeignKey(Qualifications, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']
    
    print(user)
    
    
    
    def get_absolute_url(self):
        return reverse('resume:index')
    
