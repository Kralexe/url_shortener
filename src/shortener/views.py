from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404

from .forms import SubmitUrlForm
from .models import KirrURL

def home_view_fbv(request, *args, **kwargs):
	if request.method == 'POST':
		print(request.POST)
	return render(request, 'shortener/home.html', {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			'title': 'Submit URL',
			'form': the_form,
		}
		return render(request, 'shortener/home.html', context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
		context = {
			'title': 'Submit URL',
			'form': form,
		}
		return render(request, 'shortener/home.html', context)

class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		# print(request.user)
		# print(request.user.is_authenticated)
		# print(shortcode)
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
		return HttpResponseRedirect(obj.url)