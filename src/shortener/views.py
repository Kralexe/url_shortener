from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import KirrURL

def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	# print(request.user)
	# print(request.user.is_authenticated)
	# print(shortcode)
	# obj = KirrURL.objects.get(shortcode=shortcode)

	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	# obj_url = obj.url

	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url
	return HttpResponseRedirect(obj.url)

class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		# print(request.user)
		# print(request.user.is_authenticated)
		# print(shortcode)
		return HttpResponseRedirect(obj.url)

		def post(self, request, *args, **kwargs):
			return HttpResponse()