from itertools import product
import pstats
from django.shortcuts import render
from .forms import VehicleForm
from django.http import HttpResponseRedirect
from .models import Vehicle
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import View
from django.urls import reverse
# related to user accounts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


def home(request):
    return render(request,'home.html')

def createveh(request):
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
@login_required(login_url='/')
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

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Check the login details'})
        else:
            login(request, user)
            return redirect('home')


def register(request):
    if(request.method=='GET'):
        form = UserCreationForm
        return render(request,'register.html',{'form':form})
    else:
        reg_form = UserCreationForm(request.POST)
        if(reg_form.is_valid()):
            reg_form.save()
            return redirect('loginuser')
        else:
            form = UserCreationForm
            return render(request,'register.html',{'form':form,'error':'Ensure that the password meets the criteria mentioned'})
    
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')