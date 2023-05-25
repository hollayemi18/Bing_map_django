from django.shortcuts import render, redirect
from .models import Address
from .forms import StoreData
import requests
# map function


def geocode_address(address):
    api_key = 'ArZBopFItKhshmS1NYR0zxOJ6KO5FztB-CbghO18Dfg_lhwhcdALbaieuliaynrM'
    base_url = 'http://dev.virtualearth.net/REST/v1/Locations'

    params = {
        'q': address,
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract latitude and longitude from the response
    try:
        coordinates = data['resourceSets'][0]['resources'][0]['point']['coordinates']
        latitude = coordinates[0]
        longitude = coordinates[1]
    except IndexError:
        latitude = None
        longitude = None

    return latitude, longitude
# just a form to save data


def display_map(request, id):
    user = Address.objects.get(id=id)
    stre = user.street
    city = user.city
    # concant adress from the database
    location = f"{user.street}, {user.city}, {user.country} "
    address = location
    your_address = "iwo road  ibadan nigeria"
    your_latitude, your_longitude = geocode_address(your_address)
    latitude, longitude = geocode_address(address)

    context = {
        'address': address,
        'your_address': your_address,
        'latitude': latitude,
        'longitude': longitude,
        'your_latitude': your_latitude,
        'your_longitude': your_longitude,
    }

    return render(request, 'user_map.html', context)


def emp(request):
    if request.method == "POST":
        form = StoreData(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = StoreData()
    return render(request, 'index.html', {'form': form})

# rendering of data


def show(request):
    storedata = Address.objects.all()
    return render(request, "show.html", {'storedata': storedata})
