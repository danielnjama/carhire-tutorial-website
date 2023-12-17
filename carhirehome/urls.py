from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('car/', views.car, name='car'),
    path('success/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('service/', views.service, name='service'),
    path('booking/<slug:url>', views.booking, name='booking'),
    path('car/', views.car, name='car'),
    path('car/<slug:url>', views.car_detail, name='cardetail'),
  
]