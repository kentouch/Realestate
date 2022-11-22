from distutils.command.upload import upload
from email.policy import default
from telnetlib import STATUS

from django.db import models
from django.db.models.deletion import PROTECT
from PIL import Image


# Create your models here.
class Property_status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Let's create classification: furnished and unfurnished houses as models

class Classification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

STATUS= (
    (0, 'available'),
    (1, 'sold'),
    (2, 'taken'),
    (3, 'full')
)

# category of house:house residence, Room office, room, voiture, bus

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Houses property model

class House(models.Model):
    status = models.ForeignKey(Property_status, on_delete=PROTECT, default=0)   
    availability = models.IntegerField(choices=STATUS, default=0)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=PROTECT, default=1)
    classification = models.ForeignKey(Classification, on_delete=PROTECT, default=0)
    NumbOfBeds = models.IntegerField()
    NumberOfBathrooms = models.IntegerField()
    price = models.CharField(max_length = 100)
    image_house = models.ImageField(upload_to='Images/', default='Images/house.png')
    description = models.TextField(default='house')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-uploaded_on']

    def __str__(self):
        return self.location

# Cars property model
class Car(models.Model):
    status = models.ForeignKey(Property_status, on_delete=PROTECT)
    availability = models.IntegerField(choices=STATUS, default=0)
    car_name = models.CharField(max_length=100)
    version = models.IntegerField()
   #property_stat = models.ForeignKey(Property_stat, on_delete=PROTECT, default=0)
    price = models.CharField(max_length = 100)
    image_car = models.ImageField(upload_to='Images/', blank=True, default='Images/car.png')
    description = models.TextField(default='car')
    uploaded_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering= ['-uploaded_on']

    def __str__(self):
        return self.car_name

# Fields property model
class Land(models.Model):
    status = models.ForeignKey(Property_status, on_delete=PROTECT, default=1)
    availability = models.IntegerField(choices=STATUS, default=0)
    location = models.CharField(max_length=100)
    numberOfSqrtMeter = models.IntegerField()
    price = models.CharField(max_length = 100)
    image_land = models.ImageField(upload_to='Images/', blank=True, default='Images/land.png' )
    description = models.TextField(default='house')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-uploaded_on']

    def __str__(self):
        return self.location
    
# Testimony section
class Testimony(models.Model):
    comment = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-uploaded_on']

    def __str__(self):
        return self.comment

# Images table for properties
class HouseGallery (models.Model):
    image_name = models.CharField(max_length=100)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='HousePhoto')
    photo = models.ImageField(upload_to='Images/')

    # resizing the image, you can change parameters like size and quality.
    def save(self, *args, **kwargs):
       super(HouseGallery, self).save(*args, **kwargs)
       img = Image.open(self.photo.path)
       if img.height > 700 or img.width > 600:
           img.thumbnail((700,600))
       img.save(self.photo.path,quality=70,optimize=True)

    def __str__(self):
        return self.image_name

# Cars property model
class CarGallery (models.Model):
    image_name = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='CarPhoto')
    photo = models.ImageField(upload_to='Images/')

    # resizing the image, you can change parameters like size and quality.
    def save(self, *args, **kwargs):
        super(CarGallery, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 700 or img.width > 600:
            img.thumbnail((700,600))
        img.save(self.photo.path,quality=70,optimize=True)
        
    def __str__(self):
        return self.image_name
        
            

class LandGallery (models.Model):
    image_name = models.CharField(max_length=100)
    land = models.ForeignKey(Land, on_delete=models.CASCADE, related_name='LandPhoto')
    photo = models.ImageField(upload_to='Images/')

     # resizing the image, you can change parameters like size and quality.
    def save(self, *args, **kwargs):
       super(LandGallery, self).save(*args, **kwargs)
       img = Image.open(self.photo.path)
       if img.height > 700 or img.width > 600:
           img.thumbnail((700,600))
       img.save(self.photo.path,quality=70,optimize=True)

    def __str__(self):
        return self.image_name
# End images table
