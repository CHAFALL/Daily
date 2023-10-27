from rest_framework import serializers
from .models import Weather


# ModelSerializer 인가요??
# 데이터 중에서 원하는 것이 3가지로 확정, 확정된 것만 가져다 쓸 것이라서
# 직접 필드를 지정하고 다룰것이면 Serializer로 하면 됨
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'
