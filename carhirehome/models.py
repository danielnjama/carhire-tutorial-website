from django.db import models
from datetime import datetime

ENGINE_MODE_CHOICES = (
    ('AUTO', 'Automatic'),
    ('MANUAL', 'Manual')
)

class CarGarage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Car Name')
    year = models.IntegerField(verbose_name='Year')
    fuel_consumption = models.IntegerField(verbose_name='Fuel Consumption')
    description = models.TextField(verbose_name='Car Description')
    engine_mode = models.CharField(choices=ENGINE_MODE_CHOICES, max_length=50, verbose_name='Engine Mode')
    price_per_day = models.IntegerField(verbose_name='Price Per Day')
    image = models.ImageField(upload_to='uploads', verbose_name='Image')
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    class Meta:
       verbose_name = 'Car Garage'
       verbose_name_plural = 'Car Garage'
    
class CarImages(models.Model):
    car = models.ForeignKey(CarGarage,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads',verbose_name='Image')
    def __str__(self):
        return self.car.name
    

payment_options = (
    ('Paypal','Payal'),
    ('Check','Check'),
    ('Transfer','Transfer')
)

class CarBooking(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    special_request = models.TextField()
    payment_method = models.CharField(choices=payment_options,max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name = 'Car Booking'
        verbose_name_plural = 'Car Booking'
    


class CarsRented(models.Model):
    CarBooking = models.ForeignKey(CarBooking,on_delete=models.CASCADE)
    date_out = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(default=None)
    car_returned = models.BooleanField(default=False)
    admin_comment = models.TextField()

    def __str__(self):
        return self.CarBooking.first_name
    class Meta:
       verbose_name = 'Cars Rented'
       verbose_name_plural = 'Car Rented'




