from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_task(request):
    if request.method=='POST':
        task_form = forms.TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = forms.TaskModelForm()
    return render(request,'task.html',{'form':task_form})

def edit_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form = forms.TaskModelForm(instance=task)
    if request.method=='POST':
        task_form=forms.TaskModelForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request,'task.html',{'form':task_form})

def delete_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')

def completed(request,id):
    task = models.TaskModel.objects.get(pk=id)
    task.is_completed=True
    task.save()
    return redirect('home')
