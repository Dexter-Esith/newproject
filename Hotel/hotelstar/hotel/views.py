from django.shortcuts import render, redirect
from . models import Hotel, Contact, HotelReview
from .forms import TestForm, HotelReviewForm


# Create your views here.

def homepage(request):
    hotels = Hotel.objects.all()
    reviews = HotelReview.objects.all()
    for i in reviews:
        good_hotels = ()
    for i in hotels:
        if i.stars == 5 and len(good_hotels) < 3:
            good_hotels += (i,)

    context = {
        'good_hotels' : good_hotels,
        'hotels' : hotels,
    }

    return render(request, 'hotel/index.html', context)


def about(request):
    hotels = Hotel.objects.all()
    hotel = Hotel.objects.get(id=1)
    rame = Hotel.objects.filter(stars=2)
    return render(request, 'hotel/about.html')

def services(request):
    return render(request, 'hotel/services.html')

def testimonials(request):
    return render(request, 'hotel/testimonials.html')

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
    form = TestForm()
    if request.method == "GET":
        form = TestForm(request.GET)
        if form.is_valid():
            data = form.save(commit=False)
            data.permission = True
            data.save()

            return redirect('hotel:singletest', id)


    context = {
        'contact':contact,
        'form':form,

    }
    return render(request, 'hotel/single_test.html', context)

def see_more(request, id):
    seemore = Hotel.objects.get(id=id)
    reviews = HotelReview.objects.filter(review=id)
    form = HotelReviewForm()
    if request.method == "GET":
        form = HotelReviewForm(request.GET)
        if form.is_valid():
            data = form.save(commit=False)
            data.permission = True
            data.save()

            return redirect('hotel:seemore', id)

    context = {
        'seemore':seemore,
        'reviews':reviews,
        'form':form,

    }
    return render(request, 'hotel/seemore.html', context)
