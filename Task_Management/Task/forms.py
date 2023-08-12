from django import forms
from Task.models import TaskStoreModel

class TaskStoreForm(forms.ModelForm):
    class Meta:
        model = TaskStoreModel
        fields = ['Title', 'Description']