from itertools import product
from django.shortcuts import render
from .forms import VehicleForm
from django.http import HttpResponseRedirect
from .models import Vehicle
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import View
from django.urls import reverse

def home(request):
    return render(request,'home.html')

def register(request):
    if(request.method=='GET'):
        form = VehicleForm()
        return render(request,'fillin.html',{'form':form})
    else:
        form = VehicleForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'fillin.html',{'form':form})


# def display(request):
#     all_veh_objs = Vehicle.objects.all()
#     return render(request,'display.html',{'objs':all_veh_objs})

def viewveh(request,veh_pk):
    selected_vehicle = get_object_or_404(Vehicle,pk=veh_pk)
    if(request.method=="GET"):
        selected_vehicle_form = VehicleForm(instance=selected_vehicle)
        return render(request,'viewveh.html',{'selected_vehicle_form':selected_vehicle_form})
    else:
        try:
            selected_vehicle_form = VehicleForm(request.POST,instance=selected_vehicle)
            selected_vehicle_form.save()
            return redirect('vehicleview')
        except ValueError:
            return render(request,'viewveh.html',{'selected_vehicle_form':selected_vehicle_form,'error':'Check the details entered'})


class VehicleView(View):
    def get(self,request):
        if(request.method=='GET'):
            all_veh_objs = Vehicle.objects.all()
            return render(request,'display.html',{'objs':all_veh_objs})
    def post(self,request,*args,**kwargs):
        if(request.method=='POST'):
            ids = request.POST.getlist('id[]')
            for id in ids:
                obj_to_be_deleted = Vehicle.objects.get(pk=id)
                obj_to_be_deleted.delete()
                print(f'id -> {id}')
            return HttpResponseRedirect(reverse('vehicleview'))

