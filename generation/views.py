from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from generation.models import Project, Usecase
from django.template.loader import render_to_string
from Sequenceproject.forms import ProjectForm
from django.http import JsonResponse
from django.views.generic.edit import UpdateView

def home(request):   
    tasks = Project.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'index.html', context)

def tambah_proyek(request):
    if request.method == "POST":  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/generation')  
            except:  
                return redirect('/generation') 
        else:
            return redirect('/generation') 
    else:  
        form = ProjectForm()  
    return render(request,'index.html',{'form':form})

def hapus_proyek(request, id):  
    proyek = Project.objects.get(project_id=id)  
    proyek.delete()  
    return redirect('/generation')  

def ganti_proyek(request, id):  
    proyek = Project.objects.get(project_id=id)  
    form = ProjectForm(request.POST, instance = proyek)  
    if form.is_valid():  
        form.save()  
        return redirect("/generation")  
    return render(request, 'index.html', {'proyek': proyek})

def usecase(request):   
    tasks = Usecase.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'list usecase.html', context)

def profile(request):   
    return render(request,'profile usecase.html')

def form(request):
    return render(request,'form.html')