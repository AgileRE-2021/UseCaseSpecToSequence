from django.urls import path

from . import views

app_name = 'generation'
urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('form', views.form, name='form'),
    path('tambah_proyek', views.tambah_proyek, name='tambah_proyek'),
    path('hapus_proyek/<int:id>', views.hapus_proyek),
    path('ganti_proyek/<int:id>', views.ganti_proyek),

    path('<int:project_id>/usecase', views.usecase, name='usecase'),
    path('<int:project_id>/tambah_usecase', views.tambah_usecase, name='tambah_usecase'),
    #path('<int:id>/hapus_proyek/<int:id>', views.hapus_usecase),
    #path('<int:id>/ganti_usecase/<int:id>', views.ganti_usecase),

    path('<int:project_id>/usecase/<int:usecase_id>/form', views.tambah_usecasespec, name='tambah_usecasespec')
]