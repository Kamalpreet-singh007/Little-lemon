from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # my views
    path('menu/', views.MenuItemView.as_view(), name='get_all_menu_items'),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('msg',views.msg),

    path('', include(router.urls)),
]














   # path('index/', views.index, name='index'),  # Index page
    # path('home/', views.home, name='home'),  # Home page