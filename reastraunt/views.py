from django.shortcuts import render 
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import userserializer, MenuSerializer, BokkingSerializer
from rest_framework.generics import  RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
from .models import Menu_table, Booking_table
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
# def home(request):
#     return render(request,'index.html',{})

# def index(request):
#     return HttpResponse('hello')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
    permission_classes = [IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    queryset= Booking_table.objects.all()
    serializer_class = BokkingSerializer
    permission_classes = [IsAuthenticated] 


class MenuItemView(ListCreateAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = MenuSerializer


class SingleItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = MenuSerializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
     return Response({"message":"This view is protected"})