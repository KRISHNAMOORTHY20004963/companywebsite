from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'website/home.html', context)

def productslist(request):
    context = {}
    return render(request, 'website/products.html', context)

def peoplelist(request):
    context = {}
    return render(request, 'website/people.html', context)

def contactus(request):
    context = {}
    return render(request, 'website/contactus.html', context)    