from django.shortcuts import render,get_object_or_404
from .models import Category,Products
from django.views.generic import DetailView

# Create your views here.

def index(request):
    
   
    allproducts = Products.objects.all()
    allcategory = Category.objects.all()
    context = {
        'categories' : allcategory,
        'products' : allproducts
    }
   
    return render(request,'homepage/index.html',context)


class ItemDetailView(DetailView):
    model = Products
    template_name = "homepage/product_single_view.html"





def newproducts(request):
    newproducts = Products.objects.all()
    context = {
        'newproducts' : newproducts
    }
    return render(request,'newproducts/newproducts.html',context)


def featuredproducts(request):
    fproducts  = Products.objects.all()
    context = {
        'fproducts' : fproducts
    }
    return render(request,'featuredproducts/featured.html',context)



