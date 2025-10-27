from django.shortcuts import render
from . models import Product
from . forms import ProductForm

def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product': product})
def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'add.html', {'form': ProductForm(), 'success': True})
    else:
        form = ProductForm()
    return render(request, 'add.html', {'form': form})
