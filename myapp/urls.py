from django.urls import path
from myapp.views import HomePage

urlpatterns = [
	path('', HomePage.as_view(), name='Home'),
]