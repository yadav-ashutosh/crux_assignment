from django import forms

class UploadExcel(forms.Form):
    file = forms.FileField()