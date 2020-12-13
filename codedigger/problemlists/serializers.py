from rest_framework import serializers
from .models import Problem,ProbPreCreatedList
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('name','prob_id','url','contest_id','rating','index','tags',)



class ProbPreCreatedGetListSerializer(serializers.ModelSerializer):
    # problem = ProblemSerializer(many = True)
    class Meta:
        model = ProbPreCreatedList
        fields = ('id','name','description',)


class ProbPreCreatedRetrieveListSerializer(WritableNestedModelSerializer):
    problem = ProblemSerializer(many = True)
    class Meta:
        model = ProbPreCreatedList
        fields = ('id','name','problem',)
