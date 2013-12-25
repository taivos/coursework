from django.db import models

class Gallery(models.Model):
	original = models.ImageField(upload_to = 'uploads')
	title = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title