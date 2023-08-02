from rest_framework import serializers
from home.models import home, emp


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=home
        fields=('id','name','age','dob')

