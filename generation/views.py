from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from generation.models import Project, Usecase
from django.template.loader import render_to_string
from Sequenceproject.forms import ProjectForm, UsecaseForm, UsecasespecForm
from django.http import JsonResponse
from django.views.generic.edit import UpdateView

def home(request):   
    tasks = Project.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'index.html', context)

def tambah_proyek(request):
    if request.method == 'POST':  
        form = ProjectForm(request.POST)  
        if form.is_valid():  
            print(form)
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
        return redirect('/generation')  
    return render(request, 'index.html', {'proyek': proyek})

def usecase(request, project_id):
    proyek = Project.objects.get(project_id=project_id)
    tasks = Usecase.objects.filter(project=project_id)
    context = {
        'proyek': proyek,
        'project_id': id,
        'tasks': tasks
    }
    return render(request,'list usecase.html', context)

def tambah_usecase(request, project_id):
    proyek = Project.objects.get(project_id=project_id)
    form = UsecaseForm()
    if request.method == 'POST':
        form = UsecaseForm(request.POST)
        if form.is_valid():
            formulir = form.save(commit=False)
            formulir.project = proyek
            formulir.save()
            return redirect('/generation/'+str(project_id)+'/usecase')
        else:
            print(form.errors)
            return redirect('/generation/'+str(project_id)+'/usecase')
    else:
        form = UsecaseForm()
    return render(request,'list usecase.html', {'form': form})

#def hapus_usecase(request, id):
#    proyek = Project.objects.get(project_id=id)

#def ganti_usecase(request, id):
#    proyek = Project.objects.get(project_id=id)

def form_tambah_usecasespec(request, project_id, usecase_id):
    tasks = Usecase.objects.get(usecase_id=usecase_id)   
    context = {
        'usecase_id':usecase_id,
        'project_id':project_id,
        'usecase_name':tasks.usecase_name,
        'actor':tasks.actor,
        'desc':tasks.desc,
        'postcon':tasks.postcon,
        'postcon_object':tasks.postcon_object,
        'precon':tasks.precon,
        'precon_object':tasks.precon_object
    }

    return render(request,'form.html',context)

def tambah_usecasespec(request,project_id,usecase_id):
    proyek = Usecase.objects.get(usecase_id=usecase_id)  
    form = UsecasespecForm(request.POST, instance = proyek)  
    if form.is_valid():  
        form.save()  
        return redirect('/generation/'+str(project_id)+'/usecase/'+str(usecase_id)+'/form')  

    return render(request,'form.html')

def profile(request):   
    return render(request,'profile usecase.html')

def form(request):
    return render(request,'form.html')
    