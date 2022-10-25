# forms.py
from django import forms
from .models import *

class ImageForm(forms.ModelForm):

	class Meta:
		model = Image
		fields = '__all__'
		labels = {'title': 'Image Name', 'slug': 'Re-Name', 'tags': 'Add Tags', 'pic': 'Add Image'}
		widgets ={
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter image name'}),
			'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter again image name'}),
			'tags': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter again image name', 'rows': '4'}),

		}
