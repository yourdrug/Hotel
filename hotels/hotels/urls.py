
from django.contrib import admin
from django.urls import path
from hotel.views import *

urlpatterns = [
                path('admin/', admin.site.urls),
                path('', main_page, name='home'),
                path('register/', RegisterUser.as_view(), name='register'),
                path('login/', AuthUser.as_view(), name='login'),
                path('logout/', logout_user, name='logout'),
                path('profile/', profile_page, name='profile'),
              ]
