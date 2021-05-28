from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usecase', views.usecase, name='usecase'),
    path('profile', views.profile, name='profile'),
    path('form', views.form, name='form')
]

