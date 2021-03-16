from django import forms # THIS IS FOR HAVE THE STRUCTURE OF THE FORMS
from .models import Page # THIS LINKS THE MODELS PAGE FOR GENERATE AUTOMATIC

class PageForm(forms.ModelForm): # WE CREATE THE FORM MODEL

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }
        labels = {
            'title':'','order':'','content':''
        }
