from django.contrib import admin
from . models import Hotel, Contact, HotelReview
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Contact)
admin.site.register(HotelReview)