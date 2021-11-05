from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView
from .forms import UploadImageForm
from .models import Image
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

# Create your views here.
class GalleryView(ListView, FormMixin):
	template_name = 'gallery/gallery.html'
	form_class = UploadImageForm
	success_url = reverse_lazy('gallery')
	model = Image

	def post(self, request, *args, **kwargs):
		"""
		Handle POST requests: instantiate a form instance with the passed
		POST variables and then check if it's valid.
		"""
		form = self.get_form()
		if form.is_valid():
			image = Image(
				title=self.request.POST.get('title'),
				image=self.request.FILES['file'],
			)
			image.save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
