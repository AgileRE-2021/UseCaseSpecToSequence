from django import forms
from django.db.models import fields
# import class Task dari file todo/models.py
from generation.models import Project, Usecase ,Usecasespec


# membuat class TaskForm untuk membuat task
class ProjectForm(forms.ModelForm):
    class Meta:  
        model = Project 
        fields = '__all__'

class UsecaseForm(forms.ModelForm):
    class Meta:
        model = Usecase
        fields = '__all__'
        exclude = ('project',)

class UsecasespecForm(forms.ModelForm):
    class Meta:
        model = Usecasespec
        fields = '__all__'
