from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_category(request):
    if request.method=='POST':
        category_form = forms.CategoryModelForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('home')
    else:
        category_form = forms.CategoryModelForm()
    return render(request,'category.html',{'form':category_form}) 


