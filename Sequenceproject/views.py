from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):   
    return render(request,'index.html')

def usecase(request):   
    return render(request,'list usecase.html')

def profile(request):   
    return render(request,'profile usecase.html')