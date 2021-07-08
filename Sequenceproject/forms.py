from django import forms
from django.db.models import fields
# import class Task dari file todo/models.py
from generation.models import Project, Usecase


# membuat class TaskForm untuk membuat task
class ProjectForm(forms.ModelForm):
    class Meta:  
        model = Project 
        fields = '__all__'

class UsecaseForm(forms.ModelForm):
    class Meta:
        model = Usecase
        fields = ['usecase_name']

class UsecasespecForm(forms.ModelForm):
    class Meta:
        model = Usecase
        fields = ['usecase_name','actor','desc','postcon','postcon_object','precon','precon_object']



