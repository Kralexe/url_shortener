from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

def kirr_redirect_view(request, *args, **kwargs):
	return HttpResponse('hello')

class KirrCBView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse('hello again')