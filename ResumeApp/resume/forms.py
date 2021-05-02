
from django.db.models import fields
from .models import Resume
from django import forms
from django.db.models.base import Model

class resume_form(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = "__all__"
        