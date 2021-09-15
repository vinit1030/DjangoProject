from django import forms
from crudProject.models import crudEmployee


class employeeform(forms.ModelForm):
    class Meta:
        model=crudEmployee
        fields = "__all__"