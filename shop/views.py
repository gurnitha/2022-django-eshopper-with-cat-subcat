from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')


def products(request):
	return render(request, 'products.html')


def product_detail(request):
	return render(request, 'product_detail.html')


def cart(request):
	return render(request, 'cart.html')


def contact(request):
	return render(request, 'contact.html')
