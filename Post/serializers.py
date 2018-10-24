from rest_framework import serializers
from .models import Record,Hot_50

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields=('rid', 'song_name', 'singer_name', 'song_url', 'listen_time', 'listener')


class HotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hot_50
        fields= '__all__'


class ActivitySerializer(serializers.Serializer):
    day = serializers.DateField();
    available =serializers.IntegerField();


class HourSerializer(serializers.Serializer):
    hour = serializers.IntegerField();
    available =serializers.IntegerField();