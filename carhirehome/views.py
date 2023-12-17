from django.shortcuts import render, get_object_or_404,redirect
from . models import CarGarage,CarImages,CarBooking
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail




def index(request):
    cars = CarGarage.objects.all()
    return render(request,'index.html',{'cars':cars})



def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def car(request):
    return render(request, 'car.html')

def contact(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        message = request.POST["message"]
        sender =  request.POST["email"]
        name =  request.POST["name"]
        to_email = settings.EMAIL_HOST_USER
        fmessage = "Name: {}\nEmail: {}\nMessage: {}".format(name,sender,message)
        # mail.send_mail(subject, message, sender, [to_email,])
        try:
            send_mail(subject=subject,message=fmessage,from_email=sender,recipient_list=[to_email,],fail_silently=False)
            return render(request,'success.html',{'message':'Your email has been sent!'})
        except:
            return render(request,'success.html',{'message':'Something went wrong!','status':False})
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def service(request):
    return render(request, 'service.html')

def success(request):
    return render(request, 'success.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def booking(request,url):
    car = get_object_or_404 (CarGarage, url=url)
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        special_request = request.POST['special_request']
        payment_method = request.POST['payment']
        booking_instance = CarBooking(first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,special_request=special_request,payment_method=payment_method)
        booking_instance.save()
        return render(request,'success.html',{'message':'Your car booking request has been received!'})
    return render(request, 'booking.html',{'car':car})

def car(request):
    cars = CarGarage.objects.all()
    return render(request,'car.html',{'cars':cars})


def car_detail(request,url):
    car = get_object_or_404 (CarGarage, url=url)
    car_images = CarImages.objects.filter(car=car)
    related_cars = CarGarage.objects.all().exclude(url=car.url)
    return render(request, 'detail.html', {'car': car, 'car_images': car_images,'related_cars':related_cars})
