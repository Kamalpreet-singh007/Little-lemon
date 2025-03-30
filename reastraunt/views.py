from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import userserializer, MenuSerializer, BokkingSerializer
from rest_framework.generics import  RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from .models import Menu_table, Booking_table


# Create your views here.
# def home(request):
#     return render(request,'index.html',{})

# def index(request):
#     return HttpResponse('hello')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
    # permission_classes = [permissions.IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking_table.objects.all()
    serializer_class = BokkingSerializer
    # permission_classes = [permissions.IsAuthenticated] 


class MenuItemView(ListCreateAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = MenuSerializer


class SingleItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = MenuSerializer


# class BookingTableView(ListCreateAPIView):
#     queryset= Booking_table.objects.all()
#     serializer_class = BokkingSerializer

# class SingleBookingTableView(RetrieveUpdateAPIView, DestroyAPIView):
#     queryset= Booking_table.objects.all()
#     serializer_class = BokkingSerializer