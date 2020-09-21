from django.shortcuts import render


# Create your views here.

# view for Store
def store(request):
    context = {}
    return render(request, 'store.html', context)


# View for Cart
def cart(request):
    context = {}
    return render(request, 'cart.html', context)


# View  for Checkout
def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)
