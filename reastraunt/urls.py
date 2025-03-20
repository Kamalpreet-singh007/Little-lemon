# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index),
#     path('home/',views.home, name ='home'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index page
    path('home/', views.home, name='home'),  # Home page
]