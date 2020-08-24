from django.shortcuts import render,get_object_or_404
from .models import Category,Products
from django.views.generic import DetailView,View,ListView


class Index(View):
    def get(self,request,*args,**kwargs):
        allproducts = Products.objects.all()
        allcategory = Category.objects.all()
        print(allcategory)
        context = {
            'categories' : allcategory,
            'products' : allproducts
        }
    
        return render(request,'homepage/index.html',context)






class ItemDetailView(DetailView):
    model = Products
    template_name = "homepage/product_single_view.html"
    def get_context_data(self, **kwargs):
        featuredpd = Products.objects.all()
        context = super().get_context_data(**kwargs)
        context['featuredpd'] = featuredpd
        
        return context
    




class NewProduct(ListView):
    model = Products
    template_name = 'newproducts/newproducts.html'
    context_object_name = 'newproducts'
    paginate_by = 12


class FeaturedProducts(ListView):
    model = Products
    template_name = 'featuredproducts/featured.html'
    context_object_name = 'fproducts'
    paginate_by = 12





