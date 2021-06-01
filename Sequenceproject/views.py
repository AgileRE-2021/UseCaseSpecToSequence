from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from generation.models import Project, Usecase
from django.template.loader import render_to_string
from Sequenceproject.forms import ProjectForm
from django.http import JsonResponse

def home(request):   
    proyek = Project.objects.all()
    return render(request,'index.html',{'posts':proyek})

def tambah_proyek(request):
    if request.method == "POST":  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/generation1')  
            except:  
                return redirect('/generation2') 
        else:
            return redirect('/generation3') 
    else:  
        form = ProjectForm()  
        return redirect('/generation4') 
    return render(request,'index.html',{'form':form})
    
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