from django.urls import path

from . import views

app_name = 'generation'
urlpatterns = [
    path('', views.home, name='home'),
    path('usecase', views.usecase, name='usecase'),
    path('profile', views.profile, name='profile'),
    path('form', views.form, name='form'),
    path('tambah_proyek', views.tambah_proyek, name='tambah_proyek'),
]