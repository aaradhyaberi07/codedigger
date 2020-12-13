from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import PlayList
from .serializers import PlayListGetSerializer




# Create your views here.
class PlaylistGetView(ListAPIView):
    permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = PlayListGetSerializer
    queryset = PlayList.objects.all()
  
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    