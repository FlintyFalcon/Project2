
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def showtimes(request):
	return render(request, 'showtimes.html', {})

def store(request):
	return render(request, 'store.html', {})
