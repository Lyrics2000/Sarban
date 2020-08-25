from django.shortcuts import render,get_object_or_404
from .models import Category,Products
from django.views.generic import DetailView,View,ListView
from carts.models import Cart


class Index(View):
    def get(self,request,*args,**kwargs):
        allproducts = Products.objects.all()
        allcategory = Category.objects.all()
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        cart_items  = cart_obj.products.count()
        context = {
            'categories' : allcategory,
            'products' : allproducts,
            'cart' : cart_obj,
            'cart_items' :  cart_items,
        }
    
        return render(request,'homepage/index.html',context)






class ItemDetailView(DetailView):
    model = Products
    template_name = "homepage/product_single_view.html"
    def get_context_data(self, **kwargs):
        featuredpd = Products.objects.all()
        allcategory = Category.objects.all()
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        cart_items  = cart_obj.products.count()
        context = super().get_context_data(**kwargs)
        context['featuredpd'] = featuredpd
        context['cart'] = cart_obj
        context['categories'] = allcategory
        context['cart_items'] = cart_items
        
        return context
    




class NewProduct(ListView):
    model = Products
    template_name = 'newproducts/newproducts.html'
    context_object_name = 'newproducts'
    paginate_by = 12
    def get_context_data(self, **kwargs):
        allcategory = Category.objects.all()
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        cart_items  = cart_obj.products.count()
        context = super().get_context_data(**kwargs)
        context['cart'] = cart_obj
        context['categories'] = allcategory
        context['cart_items'] = cart_items
        return context



class FeaturedProducts(ListView):
    template_name = 'featuredproducts/featured.html'
    context_object_name = 'fproducts'
    paginate_by = 12

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Products.objects.all().featured()
    def get_context_data(self, **kwargs):
        allcategory = Category.objects.all()
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        cart_items  = cart_obj.products.count()
        context = super().get_context_data(**kwargs)
        context['cart'] = cart_obj
        context['categories'] = allcategory
        context['cart_items'] = cart_items
        return context





