from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu_table, Booking_table

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['url','username', 'email', 'groups']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
      model = Menu_table
      fields = '__all__'

class BokkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_table
        fields ='__all__'