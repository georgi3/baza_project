from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('boats/', views.boats, name='boats'),
    path('parking/', views.parking, name='parking'),
    path('egery/', views.egery, name='egery'),
    path('booking/<int:pk>', views.booking, name='booking')
]