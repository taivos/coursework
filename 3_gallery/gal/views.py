# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from gal.models import Gallery

def upload(request):
	if request.method == 'POST':
		g = Gallery(original = request.FILES['image'], title = request.POST['title'])
		g.save()

		return HttpResponseRedirect("/lists")

	return render(request, 'upload.html')

def lists(request):
  context = {'lists': Gallery.objects.all()}
  return render(request, 'lists.html', context)