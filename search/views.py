from django.shortcuts import render
from django.views.generic import ListView
from products.models import Products

class SearchProductView(ListView):
    template_name = "search/view.html"
    context_object_name = 'fproducts'
    paginate_by = 12

  
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Products.objects.search(query)
        
        return Products.objects.all().featured()