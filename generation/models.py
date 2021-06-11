from django.db import models

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    project_desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project_name

class Usecase(models.Model):
    usecase_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    usecase_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    actor = models.CharField(max_length=200, blank=True)
    desc = models.CharField(max_length=200, blank=True)
    precon = models.CharField(max_length=200, blank=True)
    precon_object = models.CharField(max_length=200, blank=True)
    postcon = models.CharField(max_length=200, blank=True)
    postcon_object = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.usecase_name

class Steps(models.Model):
    step_id = models.AutoField(primary_key=True)
    spec = models.ForeignKey(Usecase, on_delete=models.CASCADE)
    is_alter = models.BooleanField()
    subject = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    object = models.CharField(max_length=200)
