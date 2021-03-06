from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html', {})


# # Describes all about our business, location, contact info, and directions to get there.
def about(request):
    return render(request, 'about.html', {})


## Describes all the movies that are currently playing, showtimes, link to buy tickets, and has thumbnail
def movies(request):
    return render(request, 'movies.html', {})


## More detail on a specific movie. Synopsis, ratings, and cast
def descriptions(request):
    return render(request, 'descriptions.html', {})


## Storefront to sell merch for our business. Shirts, mugs, stickers, gift cards.
def store(request):
    return render(request, 'store.html', {})
