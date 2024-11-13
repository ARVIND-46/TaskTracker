from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    desciption = models.TextField(blank=True)
    dueDate =models.DateField(null=True,blank=True)
    priority =models.CharField(max_length=20 ,choices=[('High','High'),('Medium','Medium'),('Low','Low')])
    Status = models.CharField(max_length=20 ,choices=[('Pending','Pending'),('Complete','Complete')])

    def __str__(self):
        return self.tittle

