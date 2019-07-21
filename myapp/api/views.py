import googlemaps
from rest_framework import viewsets
from rest_framework.response import Response
from myapp.api.serializers import TaskSerializer, initModel

tasks = {
    1: initModel(id = 1, text = 'init')
}

class TaskViewSet(viewsets.ViewSet):
	serializer_class = TaskSerializer

	def list(self, request):
		return Response({"name":"Invalid Address"})

	def create(self, request):
		my_api_key = 'AIzaSyAMWRiBXh1h0KNKSa5wq-EZILnJydUfPYc'

		gmaps = googlemaps.Client(key = my_api_key)
		data_ = request.data['text']

		try:
			g_ = gmaps.geocode(data_ + ', Bangladesh')[0]
		except:
			return Response({"name": "Not Found"})

		l_ = g_['geometry']['location']

		lat_ = l_['lat']
		lng_ = l_['lng']

		places_  = gmaps.places_nearby(location = (lat_, lng_), radius = 500, open_now = False)

		stored_ = []
		for place in places_['results']:
			id_ = place['place_id']
			fields_ = ['name']
			details_  = gmaps.place(place_id = id_, fields = fields_)
			stored_.append(details_['result'])

		return Response(stored_)