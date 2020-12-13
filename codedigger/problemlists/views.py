from django.shortcuts import render
from rest_framework import generics,status,permissions,views
from .serializers import ProbPreCreatedGetListSerializer,ProbPreCreatedRetrieveListSerializer
from .models import ProbPreCreatedList,Problem

class ProbPreCreatedGetListView(generics.ListAPIView):
    serializer_class = ProbPreCreatedGetListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()



class ProbPreCreatedListCreateView(generics.CreateAPIView):
    serializer_class = ProbPreCreatedGetListSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = ProbPreCreatedList.objects.all()

    def perform_create(self,serializer):
        return serializer.save(owner = self.request.user)


class ProbPreCreatedRetrieveListView(generics.RetrieveAPIView):
    serializer_class = ProbPreCreatedRetrieveListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProbPreCreatedList.objects.all()
    lookup_field = "id"


