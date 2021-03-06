from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('contact', views.contact, name='contact'),
    path('test', views.test, name='test'),
    path('singletest/<int:id>', views.single_test, name='singletest'),

]