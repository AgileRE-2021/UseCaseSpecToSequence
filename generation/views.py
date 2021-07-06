from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from generation.models import Project, Usecase, Steps
from django.template.loader import render_to_string
from Sequenceproject.forms import ProjectForm, UsecaseForm, UsecasespecForm
from django.http import JsonResponse
from django.views.generic.edit import UpdateView
#@register.filter

# def lookup(d, key):
#     return d[key]
def splash(request):
    return render(request, 'splash.html')

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
                return redirect('/generation/home')  
            except:  
                return redirect('/generation/home') 
        else:
            return redirect('/generation/home') 
    else:  
        form = ProjectForm()  
    return render(request,'index.html',{'form':form})

def hapus_proyek(request, id):  
    proyek = Project.objects.get(project_id=id)  
    proyek.delete()  
    return redirect('/generation/home')  

def ganti_proyek(request, id):  
    proyek = Project.objects.get(project_id=id)  
    form = ProjectForm(request.POST, instance = proyek)  
    if form.is_valid():  
        form.save()  
        return redirect('/generation/home')  
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
            return redirect('/generation/home/'+str(project_id)+'/usecase')
        else:
            print(form.errors)
            return redirect('/generation/home/'+str(project_id)+'/usecase')
    else:
        form = UsecaseForm()
    return render(request,'list usecase.html', {'form': form})

#def hapus_usecase(request, id):
#    proyek = Project.objects.get(project_id=id)

#def ganti_usecase(request, id):
#    proyek = Project.objects.get(project_id=id)

def form_tambah_usecasespec(request, project_id, usecase_id):
    tasks = Usecase.objects.get(usecase_id=usecase_id)  
    tasks2 = Steps.objects.filter(spec_id=usecase_id ,is_alter=0)
    tasks3 = Steps.objects.filter(spec_id=usecase_id ,is_alter=1)
    context = {
        'usecase_id':usecase_id,
        'project_id':project_id,
        'usecase_name':tasks.usecase_name,
        'actor':tasks.actor,
        'desc':tasks.desc,
        'postcon':tasks.postcon,
        'postcon_object':tasks.postcon_object,
        'precon':tasks.precon,
        'precon_object':tasks.precon_object,
        'steps' : tasks2,
        'steps2' : tasks3,
        'range':[1,2,3,4,5,6,7,8,9,10]
    }


        # a = tasks2[1].object
        # raise Exception()

    return render(request,'form.html',context)

def form_tambah_step(request,project_id,usecase_id):
    tasks = Steps.objects.filter(spec_id=usecase_id)  
    tasks.delete()
    for i in range(10) :
        if(bool(request.POST.get("subject_normal_"+str(i+1)) != '') and bool(request.POST.get("activity_normal_"+str(i+1)) != '') and bool(request.POST.get("activity_normal_"+str(i+1)) != '')):
            p = Steps(is_alter=request.POST.get("is_alter_normal_"+str(i+1)),subject=request.POST.get("subject_normal_"+str(i+1)),
            activity=request.POST.get("activity_normal_"+str(i+1)),object=request.POST.get("object_normal_"+str(i+1)),spec_id=usecase_id)
            p.save()
            
    for i in range(10) :
        if(bool(request.POST.get("subject_alternative_"+str(i+1)) != '') and bool(request.POST.get("activity_alternative_"+str(i+1)) != '') and bool(request.POST.get("activity_alternative_"+str(i+1)) != '')):
            p = Steps(is_alter=request.POST.get("is_alter_alternative_"+str(i+1)),subject=request.POST.get("subject_alternative_"+str(i+1)),
            activity=request.POST.get("activity_alternative_"+str(i+1)),object=request.POST.get("object_alternative_"+str(i+1)),spec_id=usecase_id)
            p.save()

    return redirect('/generation/home/'+str(project_id)+'/usecase/'+str(usecase_id)+'/form')  


def tambah_usecasespec(request,project_id,usecase_id):
    proyek = Usecase.objects.get(usecase_id=usecase_id)  
    form = UsecasespecForm(request.POST, instance = proyek)  
    if form.is_valid():  
        form.save()  
        return redirect('/generation/home/'+str(project_id)+'/usecase/'+str(usecase_id)+'/form')  

    return render(request,'form.html')

def hapus_usecase(request,project_id,usecase_id):  
    usecase = Usecase.objects.get(usecase_id=usecase_id)  
    usecase.delete()  
    return redirect('/generation/home/'+str(project_id)+'/usecase')

def generate(request, project_id, usecase_id):
    return render(request, 'generate.html')

def profile(request):   
    return render(request,'profile usecase.html')

def form(request):
    return render(request,'form.html')
    