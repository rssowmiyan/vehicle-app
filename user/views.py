from itertools import product
import pstats
from django.shortcuts import render
from .forms import VehicleForm
from django.http import HttpResponseRedirect
from .models import Vehicle,UserDetails
from django.shortcuts import get_object_or_404,redirect
from django.views.generic import View
from django.urls import reverse
# related to user accounts
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.db.models import Q

def home(request):
    return render(request,'home.html')

def createveh(request):
    if(request.method=='GET'):
        form = VehicleForm()
        return render(request,'fillin.html',{'form':form})
    else:
        form = VehicleForm(request.POST)
        if(form.is_valid()):
            brand = form.cleaned_data['brand']
            model = form.cleaned_data['model']
            owner_name = form.cleaned_data['owner_name']
            description = form.cleaned_data['description']
            special_characters = ['!','#','$','%','@','&','*','+','=','^','-']
            if(brand.isdigit() or model.isdigit() or owner_name.isdigit()):
                return render(request,'fillin.html',{'form':form,'error':'Give proper data & Check the data in brand/model/owner_name'})
            elif(set(brand).issubset(special_characters)):
                return render(request,'fillin.html',{'form':form,'error':'Brand value is invalid'})
            elif(set(model).issubset(special_characters)):
                return render(request,'fillin.html',{'form':form,'error':'Model value is invalid'})
            elif(set(owner_name).issubset(special_characters)):
                return render(request,'fillin.html',{'form':form,'error':'owner name value is invalid'})
            # atleast if everything is right    
            else:
                new_form = form.save(commit=False)
                new_form.company = request.session.get('company')
                new_form.save()
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

# used to diplay data in table
class VehicleView(View):
    def get(self,request):
        if(request.method=='GET'):
            # all_veh_objs = Vehicle.objects.all()
            currentcompany = request.session.get('company')
            all_veh_objs = Vehicle.objects.filter(company__icontains=currentcompany)
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
        company_obj = UserDetails.objects.filter(username__icontains=request.POST['username']).first()
        company_name = company_obj.company
        request.session['company'] = company_name
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
            company_name = request.POST['companyName']
            request.session['company'] = company_name
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


@login_required
def searchform(request):
    if(request.method=='POST'):
        search_term=request.POST['search_term']
        lookups= Q(brand__icontains=search_term) | Q(model__icontains=search_term) | Q(owner_name__icontains=search_term)
        search_results = Vehicle.objects.filter(lookups).distinct()
        return render(request,'display.html',{'objs':search_results})


def aboutme(request):
    return render(request,'aboutme.html')