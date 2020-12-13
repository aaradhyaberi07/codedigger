from django.contrib import admin
from django.urls import path,include
from .views import ProbPreCreatedGetListView,ProbPreCreatedListCreateView,ProbPreCreatedRetrieveListView

urlpatterns = [
    path('lists/',ProbPreCreatedGetListView.as_view(),name = 'problists'),
    path('lists/<int:id>',ProbPreCreatedRetrieveListView.as_view(),name = 'problists-id'),
    #path('lists/create/',ProbPreCreatedListCreateView.as_view(),name = 'problists-create'),
]
