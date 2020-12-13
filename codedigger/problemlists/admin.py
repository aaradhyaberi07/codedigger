from django.contrib import admin
from .models import Problem,ProbPreCreatedList
# Register your models here.
admin.site.register(ProbPreCreatedList)
admin.site.register(Problem)