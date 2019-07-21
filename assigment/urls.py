from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
    path('api/', include('myapp.api.urls')),
]
