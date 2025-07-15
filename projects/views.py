from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag,Review
from .forms import ProjectForm


# Create your views here.
def project(request):
    obj=Project.objects.all()
    context={'prjList':obj}
    return render(request,'projects/project.html',context)

def singleProject(request,pk):
    prjObj=Project.objects.get(id=pk)
    tag=prjObj.tags.all()
    context={'prjObj':prjObj,'tag':tag}
    return render(request,'projects/singleProject.html',context)

def createProject(request):
    form = ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
        else:
            print (form.error)
    context = {'form':form}
    return render(request,'projects/projectForm.html',context)

def updateProject(request,pk):
    prjObj = Project.objects.get(id=pk)
    form=ProjectForm(instance=prjObj)
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=prjObj)
        if form.is_valid():
            form.save()
            return redirect('project')
        context={'form':form}
        return render(request,'projects/updateprojectForm.html',context)

def deleteProject(request,pk):
    prjObj=Project.objects.get(id=pk)
    tag=prjObj.tags.all()
    if request.method=='POST':
        prjObj.delete()
        return redirect('project')
    context={'prjObj':prjObj,'tag':tag}
    return render(request, 'projects/deleteprojectForm.html',context)