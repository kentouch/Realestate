from tkinter import Image
from django.contrib import admin

from realest_app.models import HouseGallery, Car, CarGallery, LandGallery, Land, House, Classification, Testimony, Category, Property_status

# House optimisation for admin panel
class HouseAdmin(admin.ModelAdmin):
    list_display = ( 'location', 'classification', 'NumbOfBeds', 'NumberOfBathrooms', 'price')
    #list_filter = ['status']
    search_fields = ['location', 'classification']

# Car optimisation for admin panel
class CarAdmin(admin.ModelAdmin):
    list_display = ('status', 'car_name', 'version', 'price')
    list_filter = ['status']
    search_fields = ['status', 'car_name']

# Land optimisation for admin panel
class LandAdmin(admin.ModelAdmin):
    list_display = ('status', 'location', 'numberOfSqrtMeter', 'price')
    list_filter = ['status']
    search_fields = ['status', 'location']


# i don't understand the concept behind these classes

class HgalleryAdmin(admin.StackedInline):
    model = HouseGallery

class CgalleryAdmin(admin.StackedInline):
    model = CarGallery

class LgalleryAdmin(admin.StackedInline):
    model = LandGallery


# Register your models here.
admin.site.register(House, HouseAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(Classification)
admin.site.register(Testimony)
admin.site.register(Category)
admin.site.register(HouseGallery)
admin.site.register(CarGallery)
admin.site.register(LandGallery)
admin.site.register(Property_status)