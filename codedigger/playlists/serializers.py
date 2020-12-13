from rest_framework import serializers
from .models import PlayList
from drf_writable_nested.serializers import WritableNestedModelSerializer
from problemlists.serializers import ProblemSerializer

class PlayListGetSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many = True)
    class Meta:
        model = PlayList
        fields = ['name','description','problems']