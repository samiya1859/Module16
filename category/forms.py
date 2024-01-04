from django import forms
from .models import CategoryModel

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'