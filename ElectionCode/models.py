from django.db import models

# Create your models here.

class candidates(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    
class students(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    voted = models.BooleanField(default=False)
    student_id = models.CharField(max_length=200)
