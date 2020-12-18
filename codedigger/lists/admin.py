from django.contrib import admin
from .models import Problem,ProbPreCreatedList,Solved
# Register your models here.


class ProbAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(ProbPreCreatedList)
admin.site.register(Problem,ProbAdmin)
admin.site.register(Solved)
