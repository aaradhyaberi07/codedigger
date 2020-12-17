from django.contrib import admin
from django.urls import path,include
from .views import TopicwiseRetrieveView,TopicwiseGetView,TopicwiseLadderGetView,TopicwiseLadderRetrieveView

urlpatterns = [
    path('list/',TopicwiseGetView.as_view(),name = 'list'),
    path('list/<str:name>',TopicwiseRetrieveView.as_view(),name = 'list-name'),
    path('ladder/',TopicwiseLadderGetView.as_view(),name = 'ladder'),
    #path('ladder/<str:name>',TopicwiseLadderRetrieveView.as_view(),name = 'ladder-name'),
]
