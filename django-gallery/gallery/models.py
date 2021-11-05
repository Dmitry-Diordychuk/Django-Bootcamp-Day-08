from django.db import models

# Create your models here.
class Image(models.Model):
	title = models.CharField(null=False, max_length=50)
	image = models.FileField(upload_to='images')
