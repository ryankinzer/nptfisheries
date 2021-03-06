from django import forms
from main.models import Division, Project

class DivisionForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    director = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    deputy = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    support = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Division
        fields = ('name', 'description', 'director', 'deputy', 'support', 'phone_number',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('division', 'name', 'description', 'projectleader', 'created', 'inactive',)

        widgets = {
            'division': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'projectleader': forms.TextInput(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'class': 'form-control'}),
           # 'inactive': forms.RadioSelect(attrs={'class': 'form-control', 'type':'checkbox'}),
        }