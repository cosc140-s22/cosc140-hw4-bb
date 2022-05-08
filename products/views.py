from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def index(request):
  products = Product.objects.all().order_by('name')
  context = {'products': products}
  response = render(request, "products/index.html", context)
  return response

  
def show(request,pid):
 product = get_object_or_404(Product, pk=pid)
 context = {'products': product}
 response = render(request, 'products/show.html', context)
 return response

# Create your views here.
