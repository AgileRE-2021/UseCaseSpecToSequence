from django.urls import path

from . import views

app_name = 'generation'
urlpatterns = [
    path('', views.splash, name='splash'),
    path('home', views.home, name="home"),
    path('profile', views.profile, name='profile'),
    path('form', views.form, name='form'),
    path('tambah_proyek', views.tambah_proyek, name='tambah_proyek'),
    path('hapus_proyek/<int:id>', views.hapus_proyek),
    path('ganti_proyek/<int:id>', views.ganti_proyek),

    path('home/<int:project_id>/usecase', views.usecase, name='usecase'),
    path('home/<int:project_id>/tambah_usecase', views.tambah_usecase, name='tambah_usecase'),
    path('home/<int:project_id>/hapus_usecase/<int:usecase_id>', views.hapus_usecase, name='hapus_usecase'),
    #path('<int:id>/ganti_usecase/<int:id>', views.ganti_usecase),

    path('home/<int:project_id>/usecase/<int:usecase_id>/form', views.form_tambah_usecasespec, name='form_tambah_usecasespec'),
    path('home/<int:project_id>/<int:usecase_id>/tambah_usecasespec', views.tambah_usecasespec, name='tambah_usecasespec'),
    path('home/<int:project_id>/<int:usecase_id>/tambah_step', views.form_tambah_step, name='form_tambah_step'),

    path('home/generate', views.generate, name='generate')
    
]