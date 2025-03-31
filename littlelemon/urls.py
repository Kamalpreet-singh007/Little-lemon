from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from reastraunt.views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('reastraunt.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('booking/',include(router.urls)),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),

    
    path('api-token-auth',obtain_auth_token),

]
