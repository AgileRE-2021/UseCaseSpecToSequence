from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from .models import Project


# membuat class TaskForm untuk membuat task
class ProjectForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = Project
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('project_name', 'project_desc')
        # mengatur teks label untuk setiap field
        labels = {
            'project_name': _('Nama Proyek'),
            'project_desc': _('Deskripsi Proyek'),
        }
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'project_name': {
                'required': _("Judul harus diisi."),
            },
            'project_desc': {
                'required': _("Deskripsi harus diisi."),
            },
        }