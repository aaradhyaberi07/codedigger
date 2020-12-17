from django.shortcuts import render
from rest_framework import generics,status,permissions,views
from .serializers import TopicwiseGetSerializer,TopicwiseRetrieveSerializer,TopicwiseLadderRetrieveSerializer
from .models import ProbPreCreatedList,Problem,Solved

class TopicwiseGetView(generics.ListAPIView):
    serializer_class = TopicwiseGetSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()




class TopicwiseRetrieveView(generics.RetrieveAPIView):
    serializer_class = TopicwiseRetrieveSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()
    lookup_field = "name"

    def get_serializer_context(self,**kwargs):
        data = super().get_serializer_context(**kwargs)
        data['user'] = self.request.user.username
        return data


class TopicwiseLadderGetView(generics.ListAPIView):
    serializer_class = TopicwiseGetSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()



class TopicwiseLadderRetrieveView(generics.RetrieveAPIView):
    serializer_class = TopicwiseLadderRetrieveSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()
    lookup_field = "name"

    def get_serializer_context(self,**kwargs):
        data = super().get_serializer_context(**kwargs)
        data['user'] = self.request.user.username
        for prob in queryset.problem.all():
            exists = Solved.objects.filter(user__username = self.request.user.username,problem=prob).exists()
            if not exists:
                data['prob'] = prob
                break
        return data
        

