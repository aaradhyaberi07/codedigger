from rest_framework import serializers
from .models import Problem,ProbPreCreatedList,Solved
from drf_writable_nested.serializers import WritableNestedModelSerializer
import json

class ProblemSerializer1(serializers.ModelSerializer):
    solved = serializers.SerializerMethodField()


    def get_solved(self,obj):
        user = self.context["user"]
        solve = Solved.objects.filter(user__username=user,problem = obj)
        if solve.exists():
            return True
        return False





    class Meta:
        model = Problem
        fields = ('id','name','prob_id','url','contest_id','rating','index','tags','solved')

class ProblemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id','name','prob_id','url','contest_id','rating','index','tags')



class TopicwiseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProbPreCreatedList
        fields = ('id','name','description',)


class TopicwiseRetrieveSerializer(WritableNestedModelSerializer):
    user = serializers.SerializerMethodField()
    problem = ProblemSerializer1(many = True,context = {'user' : user})
    def get_user(self,attrs):
        user = self.context.get('user')
        return user

    class Meta:
        model = ProbPreCreatedList
        fields = ('id','user','name','description','problem',)

class TopicwiseLadderRetrieveSerializer(WritableNestedModelSerializer):
    user = serializers.SerializerMethodField()
    problem = serializers.SerializerMethodField()
    #problem = serializers.SerializerMethodField()

    def get_user(self,attrs):
        user = self.context.get('user')
        return user

    def get_problem(self,attrs):
        qs = self.context.get['prob']
        return ProblemSerializer2(qs,many=True).data
    # def get_problem(self,obj):
    #     user = self.context.get('user')
    #     for prob in obj.problem.all():
    #         exist,created = Solved.objects.get_or_create(user__username = user,problem = prob)
    #         if created:
    #             return prob
                


    class Meta:
        model = ProbPreCreatedList
        fields = ('id','user','name','description','problem',)