from django import forms

class fileUploadForm(forms.Form):
        file_name = forms.CharField(widget = forms.TextInput(attrs= {'class' : 'form-control'}))
        the_file = forms.FileField(widget = forms.FileInput(attrs= {'class' : 'form-control'}))
