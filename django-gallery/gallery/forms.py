from django import forms

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
		'class': "form-control",
		'id': "imageInputTitle",
	}))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={
		'class': "form-control",
		'id': "imageInputUpload",
	}))
