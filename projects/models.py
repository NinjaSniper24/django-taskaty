from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

class Category(models.Model) :
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Status(models.IntegerChoices):
    PENDING = 1 , 'Pending'
    COMPLETED = 2 , 'Completed'
    POSTPONED = 3 , 'Postponed'
    CANDELED = 4 , 'Canceled'

class Project(models.Model) :
    title = models.CharField( max_length=50)
    description = models.TextField()
    status = models.IntegerField(choices = Status.choices, default = Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT )
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE , null= True)

    def __str__(self) :
        return self.title
    
class Task(models.Model) :
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    status = models.IntegerField(choices = Status.choices, default = Status.PENDING)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.description