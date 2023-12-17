from django.contrib import admin
from . models import CarGarage,CarImages,CarBooking,CarsRented


class CarBookingAdmin(admin.ModelAdmin):
    list_display = ['first_name','email','phone_number','date','payment_method']

class CarsRentedAdmin(admin.ModelAdmin):
    list_display = ['CarBooking','date_out','date_returned','car_returned']

class CarGarageAdmin(admin.ModelAdmin):
    list_display = ['name','year','fuel_consumption','engine_mode','price_per_day']
    prepopulated_fields = {'url':('name',)}

admin.site.register(CarGarage,CarGarageAdmin)
admin.site.register(CarImages)
admin.site.register(CarBooking,CarBookingAdmin)
admin.site.register(CarsRented,CarsRentedAdmin)
