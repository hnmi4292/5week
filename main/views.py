from django.shortcuts import render, redirect
from .models import Product, Get
from rest_framework import viewsets
from .serializers import GetProductSerializer, PostProducerSerializer


class GetViewSet(viewsets.ModelViewSet):
    queryset = Get.objects.all()
    serializer_class = GetProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PostProducerSerializer


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    productlist = Product.objects.all()

    return render(request, 'main/blog.html', {'productlist': productlist})


def posting(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'product': product})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Product.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                price=request.POST['price'],
            )
        else:
            new_article = Product.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                price=request.POST['price'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Product': product})


######################################################################

def sellblog(request):
    productlist = Product.objects.all()

    return render(request, 'main/sellblog.html', {'productlist': productlist})


def sell_posting(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'product': product})


def new_get(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article = Product.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                price=request.POST['price'],
            )
        else:
            new_article = Product.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
                price=request.POST['price'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_get.html')


def remove_get(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/sellblog/')
    return render(request, 'main/remove_get.html', {'Product': product})
