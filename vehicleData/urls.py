from socket import IPPORT_RESERVED
from django.contrib import admin
from django.urls import path
from user import views
from user.views import VehicleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('create/',views.register,name='register'),
    path('read/',VehicleView.as_view(),name='vehicleview'),
    # path('read/',views.display,name='display'),
    path('veh/<int:veh_pk>',views.viewveh,name='viewveh'),
    # path('delete/',DeleteVehicle.as_view(),name='deletevehicle')
]
