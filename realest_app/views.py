from multiprocessing import context
from re import template

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

#from django.views.generic.detail import CreateView
from .forms import CommentForm
from .models import (Car, CarGallery, House, HouseGallery, Land, LandGallery,
                     Testimony)

# Create your views here.

def index(request):
   # myproperties= Houses.objects.all().values()
    myHouses= House.objects.all().values().order_by('-uploaded_on')
    myCars= Car.objects.all().values()
    myLands= Land.objects.all().values()
    template = loader.get_template('index.html')

    context={
       # 'myproperties' : myproperties,
        'myHouses': myHouses,
        'myCars' : myCars,
        'myLands': myLands,
    }

    return HttpResponse(template.render(context, request))

def properties(request):
    houses= House.objects.all().values()
    car = Car.objects.all().values()
    land = Land.objects.all().values()
    template = loader.get_template('properties.html') 
    context= {
        'houses': houses,
        'cars':car,
        'lands':land
    }
    return HttpResponse(template.render(context, request))
 # Adding a new record of a property in the database   

def contact(request):
     # CONTACT FORM
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        send_mail(
            'Message from ' + name,
            message,
            email,
            ['ruzindanakent.rk@gmail.com']
        )
        
    return render(request, 'Contact.html', {})


# pass id attribute from urls
def add_comment(request):
    comments = 'Hello'
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.cleaned_data['comment']
            
    else:
        form= CommentForm()

    
    return render(request, 'Add_comment.html', {'comments':comments})
        
 
# Houses detail view
def houseDetail_view(request, id):
    house = House.objects.get(id=id)
    house_gallery= HouseGallery.objects.filter(house=house)
    context = {
        'house':house,
        'house_gallery':house_gallery
    }
    return render(request, 'Housedetail.html', context)

# Cars detail view
def carDetail_view(request, id):
    car = Car.objects.get(id=id)
    car_gallery= CarGallery.objects.filter(car=car)
    context = {
        'car':car,
        'car_gallery':car_gallery
    }
    return render(request, 'Cardetail.html', context)

# Lands detail view
def landDetail_view(request, id):
    land = Land.objects.get(id=id)
    land_gallery= LandGallery.objects.filter(land=land)
    context = {
        'land':land,
        'land_gallery':land_gallery
    }
    return render(request, 'LandDetail.html', context)

def search_bar(request):
    if request.method == 'POST':
        search = request.POST['search']
        house = House.objects.filter(location__contains=search)
        car = Car.objects.filter(car_name__contains=search)
        land = Land.objects.filter(location__contains=search)
        return render(request, 'search_results.html', {'search':search, 
                                                        'house': house,
                                                        'car': car,
                                                        'land': land,
                                                         })
    else:
        return render(request, 'search_results.html', {})


# Delete e record of a property 

#def delete(request, id):
    #property = Property.objects.get(id=id)
    #property.delete()
    #return HttpResponseRedirect(reverse('index'))

# Update new property through another template via a form
def about(request):
    template = loader.get_template('About.html')
    return HttpResponse(template.render({}, request))

# Registration of new Update property the property record

#def updateProperty(request, id):
    #upd_property = Property.objects.get(id=id)
    ##x1=request.POST['location']
    #y1=request.POST['status']
    #z1=request.POST['price']
    #upd_property.property_location = x1
    #upd_property.property_status = y1
    #upd_property.property_price = z1
    #upd_property.save()

# DESCENDING ORDER QUERY
## mydata = Members.objects.all().order_by('-firstname').values()
## Members.objects.all().order_by('lastname', '-id').values()
