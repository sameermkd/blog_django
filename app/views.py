from django.shortcuts import render, get_object_or_404, redirect
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
def show(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'show.html', {'product': product})
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form, 'product': product})
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'delete.html', {'product': product})
