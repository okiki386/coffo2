from django.shortcuts import render 
from .models import BlogPost
from .models import Product
from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    products = Product.objects.order_by('-created_at')[:4]
    posts = BlogPost.objects.order_by('-created_date')[:3]

    context = {    
        'products': products,  
        'posts': posts,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)

    context = {
        'post': post
    }
    return render (request, 'pages/blog-detail.html', context)



def contact(request):
    return render(request, 'pages/contact.html')

def coffee(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 2) 
    # show 8 products per page
    page = request.GET.get('page')
    try :
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer,deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        #If page is out of range (e.g. 9999), deliver last page of results
        products = paginator.page(paginator.num_pages)

    context = {
        'products':products
    }

    return render(request, 'pages/coffees.html', context)

def shop_detail(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product': product
    }
    return render(request, 'pages/shop_detail.html', context)
