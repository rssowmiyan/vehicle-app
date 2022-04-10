from django.contrib import admin
from django.urls import path,include
from user import views
from user.views import VehicleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('create/',views.createveh,name='createveh'),
    path('read/',VehicleView.as_view(),name='vehicleview'),
    path('veh/<int:veh_pk>',views.viewveh,name='viewveh'),
    path('search/',views.searchform,name='searchform'),
    # Authentication
    path('accounts/register',views.register,name='register'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('about/',views.aboutme,name='aboutme'),
]
