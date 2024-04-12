from django.db import models

# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=50,primary_key=True)
    sprinciple=models.CharField(max_length=50)
    scontact=models.CharField(max_length=50)

    def __str__(self):
        return self.sname