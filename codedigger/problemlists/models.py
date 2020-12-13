from django.db import models
from users.models import User


class Problem(models.Model):
    name = models.CharField(max_length = 100,default = "")
    prob_id = models.CharField(max_length=500,default = "")
    url = models.CharField(max_length=500,default= "")
    tags = models.CharField(max_length = 500,default = "")
    contest_id = models.CharField(max_length=100,default="")
    index = models.CharField(max_length=5,default="")
    rating = models.CharField(max_length=10,default="")
    #solved = models.ManyToManyField(Solved,related_name="solved")
    def __str__(self):
        return self.name
    


class ProbPreCreatedList(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    problem = models.ManyToManyField(Problem,related_name="list",blank = True)
    name = models.CharField(max_length=100,default = "")
    description = models.TextField(max_length = 500,default="")
    ladder = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    

class Solved(models.Model):
    solved = models.BooleanField(default = False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    #problem = foreign key
    def __str__(self):
        return solved 