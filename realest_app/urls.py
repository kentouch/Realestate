from django.urls import path
from . import views

# urls section
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('house_detail/<int:id>', views.houseDetail_view, name='house-detail'),
    path('car_detail/<int:id>', views.carDetail_view, name='car-detail'),
    path('land_detail/<int:id>', views.landDetail_view, name='land-detail'),
    path('search/', views.search_bar, name='search-results'),
    #path('delete/<int:id>', views.delete, name='delete'),
    #path('update/<int:id>', views.about, name='update'),
    #path('update/updateProperty/<int:id>', views.updateProperty, name='updateProperty'),
    path('properties/', views.properties, name='properties'),
    path('add_comment/', views.add_comment, name='comment_section'),
]
