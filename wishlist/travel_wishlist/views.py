from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf.urls import url
from .models import Place
from .forms import NewPlaceForm, ShowPlaceInfoForm
# Create your views here.

def place_list(request):
    # Post request
    ### Make sure POST is alwayse caps ###
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    # If not a POST request, or the form is not valid, display the page with the form, and place list
    places = Place.objects.filter(visited=False)
    form = NewPlaceForm()
    return render(request, 'travel_wishlist\wishlist.html', {'places': places, 'form': form})

# Slide 58
def places_visited(request):

    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited':visited})

def place_is_visited(request):

    if request.method == "POST":
        pk = request.POST.get('pk')
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')

def place_info(request, pk):
    if request.method == "GET":
        place = get_object_or_404(Place, pk=pk)
        form = ShowPlaceInfoForm()
        return render(request, 'travel_wishlist\place_info.html', {'place':place, 'form':form})

def update_place_info(request):
    if request.method == "POST":
        form = ShowPlaceInfoForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')
        return render(request, 'travel_wishlist\place_info.html', {'place':place, 'form':form})
