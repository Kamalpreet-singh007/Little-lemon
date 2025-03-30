from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    # my views
    # path('booking-table',views.BookingTableView.as_view()),
    # path('booking-table/<int:pk>',views.SingleBookingTableView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),




    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]















   # path('index/', views.index, name='index'),  # Index page
    # path('home/', views.home, name='home'),  # Home page