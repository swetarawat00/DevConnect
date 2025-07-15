from django.urls import path
from . import views

urlpatterns = [
    path('', views.project,name='project'),
    path('singleProject/<str:pk>/',views.singleProject,name='singleProject'),
    path('createProject/',views.createProject,name='createProject'),
    path('updateProject/<str:pk>/',views.updateProject,name='updateProject'),
    path('deleteProject/<str:pk>/',views.deleteProject,name='deleteProject')
]