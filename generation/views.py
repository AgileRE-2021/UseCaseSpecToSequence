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

def translasi(usecase_id):
    # Ambil object
    u = Usecase.objects.get(usecase_id=usecase_id)
    s = Steps.objects.filter(spec=usecase_id)

    # Variabel objek-objek untuk dimasukkan ke dalam UMLscript
    actor = '"' + u.actor + '"'
    usecase = '"' + u.usecase_name.replace(" ", "") + "Controller" + '"'
    precon_obj = '"' + u.precon_object + '"'
    postcon_obj = '"' + u.postcon_object + '"'

    # Dictionary
    objek = {
        "actor": "actor",
        "usecase": "control",
        "precon_obj": "boundary",
    }
    if "Database" in postcon_obj or "database" in postcon_obj:
        objek["postcon_obj"] = "entity"
    else:
        objek["postcon_obj"] = "boundary"

    # List langkah-langkah untuk tiap bagian
    step_subjects = list(s.values_list("subject", flat=True))
    step_activities = list(s.values_list("activity", flat=True))
    step_objects = list(s.values_list("object", flat=True))
    step_alter = list(s.values_list("is_alter", flat=True))

    # List hasil translasi dan interaksi untuk objek-objek
    hasil_translasi = ["@startuml"]
    translasi_steps = list(range(len(s)))

    # UMLscript
    hasil_translasi.append("actor " + actor)
    hasil_translasi.append("boundary " + precon_obj)
    hasil_translasi.append("control " + usecase)
    if objek["postcon_obj"] == "entity":
        hasil_translasi.append("entity " + postcon_obj)
    else:
        hasil_translasi.append("boundary " + postcon_obj)

    # Loop untuk seluruh langkah-langkah dalam satu use case
    # Aturan hubungan diagram sequence: actor->boundary, boundary->control, control->boundary atau entity, entity->control
    for i in translasi_steps:
        if step_alter[i] == False: # Skenario normal
            if step_subjects[i] == u.actor: # Jika subjek langkah adalah aktor
                if step_objects[i] == u.postcon_object and objek["postcon_obj"] == "boundary":
                    translasi_steps[i] = actor + "->" + postcon_obj + ": " + step_activities[i] # actor->boundary
                else:
                    translasi_steps[i] = actor + "->" + precon_obj + ": " + step_activities[i] # actor->boundary
            else:
                if step_subjects[i-1] == u.actor:
                    if str(u.precon_object) in translasi_steps[i-1]:
                        translasi_steps[i] = precon_obj + "->" + usecase + ": " + step_activities[i] # boundary->control
                    elif str(u.postcon_object) in translasi_steps[i-1]:
                        translasi_steps[i] = postcon_obj + "->" + usecase + ": " + step_activities[i] # boundary->control atau entity->control
                elif step_objects[i] == actor:
                    if step_objects[i-1] == u.precon_object:
                        translasi_steps[i] = precon_obj + "->" + actor + ": " + step_activities[i] # boundary->control
                    elif step_objects[i-1] == u.postcon_object and objek["postcon_obj"] == "boundary":
                        translasi_steps[i] = postcon_obj + "->" + actor + ": " + step_activities[i] # boundary->control
                else:
                    if step_objects[i] == u.precon_object: 
                        translasi_steps[i] = usecase + "->" + precon_obj + ": " + step_activities[i] # control->boundary
                    elif step_objects[i] == u.postcon_object:
                        translasi_steps[i] = usecase + "->" + postcon_obj + ": " + step_activities[i] # control->boundary atau control->entity
        elif step_alter[i] == True: # Skenario alternatif
            if step_subjects[i] == u.actor: # Jika subjek langkah adalah aktor
                if step_objects[i] == u.postcon_object and objek["postcon_obj"] == "boundary":
                    translasi_steps[i] = actor + "->" + postcon_obj + ": " + step_activities[i] # actor->boundary
                else:
                    translasi_steps[i] = actor + "->" + precon_obj + ": " + step_activities[i] # actor->boundary
            else:
                if str(u.precon_object) in step_objects[i]:
                    translasi_steps[i] = precon_obj + "->" + usecase + ": " + step_activities[i] # boundary->control
                elif str(u.postcon_object) in step_objects[i]:
                    translasi_steps[i] = postcon_obj + "->" + usecase + ": " + step_activities[i] # boundary->control atau entity->control
                elif step_objects[i] == actor:
                    if step_objects[i-1] == u.precon_object:
                        translasi_steps[i] = precon_obj + "->" + actor + ": " + step_activities[i] # boundary->control
                    elif step_objects[i-1] == u.postcon_object and objek["postcon_obj"] == "boundary":
                        translasi_steps[i] = postcon_obj + "->" + actor + ": " + step_activities[i] # boundary->control
                else:
                    if step_objects[i] == u.precon_object: 
                        translasi_steps[i] = usecase + "->" + precon_obj + ": " + step_activities[i] # control->boundary
                    elif step_objects[i] == u.postcon_object:
                        translasi_steps[i] = usecase + "->" + postcon_obj + ": " + step_activities[i] # control->boundary atau control->entity

    # Menambahkan kata end jika ada skenario alternatif
    #if True in step_alter:
    #    translasi_steps.append("alt alternative")
    #    translasi_steps.append("end")

    # Menghilangkan angka dalam list translasi_steps
    #for i in translasi_steps:
    #    if isinstance(i, int):
    #        del translasi_steps[i]

    # Pengurutan hasil translasi
    hasil_translasi.extend(translasi_steps)
    hasil_translasi.append("@enduml")
    print("\n".join(str(v) for v in hasil_translasi))
    return hasil_translasi
    return print("\n".join(str(v) for v in hasil_translasi))

def hapus_usecase(request,project_id,usecase_id):  
    usecase = Usecase.objects.get(usecase_id=usecase_id)  
    usecase.delete()  
    return redirect('/generation/home/'+str(project_id)+'/usecase')

def generate(request, project_id, usecase_id):
    context = {
        'hasil_translasi' : translasi(usecase_id)
    }
    #raise Exception()
    return render(request, 'generate.html' , context)

def profile(request):   
    return render(request,'profile usecase.html')

def form(request):
    return render(request,'form.html')
    