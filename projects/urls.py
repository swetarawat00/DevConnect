from django.urls import path
from . import views

urlpatterns = [
    path('', views.project,name='project'),
    path('singleProject/<str:pk>/',views.singleProject,name='singleProject'),
    
]