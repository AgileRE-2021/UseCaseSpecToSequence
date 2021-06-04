from django import forms
# import class Task dari file todo/models.py
from generation.models import Project, Usecase


# membuat class TaskForm untuk membuat task
class ProjectForm(forms.ModelForm):
    class Meta:  
        model = Project 
        fields = "__all__"

class UsecaseForm(forms.ModelForm):
    class Meta:
        model = Usecase
        fields = "__all__"
