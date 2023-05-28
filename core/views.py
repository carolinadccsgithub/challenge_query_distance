import geopy.geocoders
from django.contrib import messages
from django.shortcuts import render
from geopy import distance
from geopy.geocoders import Nominatim


from .forms import QueryDistanceForm
from .models import QueryDistance


# Create your views here.
def index(request):
    form = QueryDistanceForm(request.POST or None)

    #address = '4790 W 16th St, Indianapolis, IN 46222'
    #address2 = '2920 Zoo Dr, San Diego, CA 92101'

    if str(request.method == 'POST'):
        if form.is_valid():
            source = form.cleaned_data['source_address']
            destination = form.cleaned_data['destination_address']
            source_address = Nominatim(user_agent='tutorial').geocode(source)
            destination_address = Nominatim(user_agent='tutorial').geocode(destination)
            dist = distance.distance((source_address.latitude, source_address.longitude), (destination_address.latitude,destination_address.longitude)).kilometers
            distances_obj = QueryDistance(source_address=source_address.address, destination_address=destination_address.address, distance=dist)
            distances_obj.save()
            text = "Distance in kilometers between these tow addresses: " + str(dist)
            messages.success(request, text)
            form = QueryDistanceForm()
        else:
            messages.error(request, 'Error to query distance')

    context = {
        'form' : form
    }
    return render(request, 'index.html', context)


def historical(request):
    distances = QueryDistance.objects.all()
    context = {
        'distances': distances
    }
    return render(request, 'historical.html', context)

