import requests
from django.shortcuts import render
from django.views.generic import ListView

class HomePage(ListView):
	template_name = 'index.html'
	context_object_name = 'places'

	def get_queryset(self):
		queryset = self.request.GET.get("text")
		if(queryset):
			queryset = requests.post('http://127.0.0.1:8000/api/location/', {"text" : queryset}).json()
		return queryset