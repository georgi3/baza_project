from django.contrib import admin
from .models import Rooms, Booking


class RoomsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'starting_date', 'end_date', 'total_sum']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Rooms, RoomsAdmin)
