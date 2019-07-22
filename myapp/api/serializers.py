from rest_framework import serializers

class initModel(object):
    def __init__(self, **kwargs):
        for field in ('id', 'text'):
            setattr(self, field, kwargs.get(field, None))

class LocationSerializer(serializers.Serializer):
	text = serializers.CharField(max_length=256)

	def create(self, validated_data):
		return initModel(id = None, **validated_data)


