from django.db import models
from users.models import User
from problemlists.models import Problem


class PlayList(models.Model):
    name = models.CharField(max_length=100,default=" ")
    description = models.TextField(max_length=200,default=" ")
    owner = models.ManyToManyField(User,related_name = "Owner")
    problems = models.ManyToManyField(Problem,related_name="Problem",null=True,blank=True)

    def __str__(self):
        return str(self.owner) + "'s Playlist"
    
    