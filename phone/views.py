from django.shortcuts import render, redirect
from .models import Document

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_option = request.GET.get('sort')
    template = 'catalog.html'
    if sort_option == 'name':
        phones = Document.objects.all().order_by('name')
    elif sort_option == 'min_price':
        phones = Document.objects.all().order_by('price')
    elif sort_option == 'max_price':
        phones = Document.objects.all().order_by('-price')
    else:
        phones = Document.objects.all()

    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Document.objects.get(slug=slug)
    context = {"phone": phone}
    return render(request, template, context)
