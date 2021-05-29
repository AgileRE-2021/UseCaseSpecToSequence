from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Project, Usecase
from django.template.loader import render_to_string
from .forms import ProjectForm
from django.http import JsonResponse

def home(request):   
    tasks = Project.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request,'index.html', context)

def tambah_proyek(request):
    data = dict()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ProjectForm()

    context = {'form': form}
    data['html_form'] = render_to_string('generation/index.html',
        context,
        request=request
    )
    return JsonResponse(data)
    return JsonResponse({'html_form': html_form})
    
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