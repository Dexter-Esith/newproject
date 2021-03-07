from django.shortcuts import render
from . models import Hotel, Contact, HotelReview
# Create your views here.
def homepage(request):
    hotels = Hotel.objects.all()
    reviews = HotelReview.objects.all()
    for i in reviews:
        print(i.review.stars)
    good_hotels = ()
    for i in hotels:
        if i.stars == 5 and len(good_hotels) < 3:
            good_hotels += (i,)
    print(good_hotels)


    context = {
        'good_hotels' : good_hotels,
        'hotels' : hotels,
    }

    return render(request, 'hotel/index.html', context)


def about(request):
    hotels = Hotel.objects.all()
    print(hotels)
    hotel = Hotel.objects.get(id=1)
    print(hotel)
    rame = Hotel.objects.filter(stars=2)
    return render(request, 'hotel/about.html')

def services(request):
    return render(request, 'hotel/services.html')

def testimonials(request):
    contacts = Contact.objects.all()
    print(contacts)
    context = {
        'contacts' : contacts,
    }
    return render(request, 'hotel/testimonials.html', context)

def contact(request):
    return render(request, 'hotel/contact.html')

def test(request):
    hotels = Hotel.objects.all()
    bad_hotels = ()
    shit_hotels = ()

    for i in hotels:
        if i.hotel_type == "1":
            bad_hotels += (i,)

            print(bad_hotels)
        else:
            shit_hotels += (i,)

            print(shit_hotels)


    print(bad_hotels)
    context = {
        'hotels' : hotels,
        'bad_hotels' : bad_hotels,
        'shit_hotels' : shit_hotels,
    }
    return render(request, 'hotel/test.html', context)


def single_test(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact':contact,

    }
    return render(request, 'hotel/single_test.html', context)

def see_more(request):
    seemore = Hotel.objects.all()
    context = {
        'seemore':seemore,

    }
    return render(request, 'hotel/seemore.html', context)
