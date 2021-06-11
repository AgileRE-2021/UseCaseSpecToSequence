from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from generation.models import Project, Usecase
from django.template.loader import render_to_string
from Sequenceproject.forms import ProjectForm, UsecaseForm
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

def tambah_usecasespec(request, project_id, usecase_id):

    tasks = Usecase.objects.get(usecase_id=usecase_id)
    if request.method == 'GET' :
        form = UsecaseForm(request.GET)
        context = {
            'tasks' : tasks,
            'usecase_name' : request.GET.get('usecase_name'),
            'actor' : request.GET.get('actor'),
            'desc' : request.GET.get('desc'),
            'precon' : request.GET.get('precon'),
            'precon_object' : request.GET.get('precon_object'),
            'postcon' : request.GET.get('postcon'),
            'postcon_object' : request.GET.get('postcon_object')
        }
        if form.is_valid() :
            form.save()
            return render(request,'form.html',context)
    

    return render(request,'form.html')

def profile(request):   
    return render(request,'profile usecase.html')

def form(request):
    return render(request,'form.html')
    