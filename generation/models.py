from django.db import models

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=200)
    
    def __str__(self):
        return self.project_name

class Usecase(models.Model):
    usecase_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    usecase_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.usecase_name

class Usecasespec(models.Model):
    spec_id = models.AutoField(primary_key=True)
    usecase = models.ForeignKey(Usecase, on_delete=models.CASCADE)
    spec_actor = models.CharField(max_length=200)
    spec_desc = models.CharField(max_length=200)
    spec_precon = models.CharField(max_length=200)
    spec_precon_object = models.CharField(max_length=200)
    spec_postcon = models.CharField(max_length=200)
    spec_postcon_object = models.CharField(max_length=200)

class Steps(models.Model):
    step_id = models.AutoField(primary_key=True)
    spec = models.ForeignKey(Usecasespec, on_delete=models.CASCADE)
    is_alter = models.BooleanField()
    subject = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    object = models.CharField(max_length=200)
