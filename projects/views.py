from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tag,Review


# Create your views here.
def project(request):
    obj=Project.objects.all
    context={'prjList':obj}
    return render(request,'projects/project.html',context)

def singleProject(request,pk):
    prjObj=Project.objects.get(id=pk)
    tag=prjObj.tags.all()
    conetxt={'prjObj':prjObj,'tag':tag}