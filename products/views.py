from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def shop(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 2)
    page = request.GET.get('page', 1)
    pages = paginator.get_page(page)
    context = {'products': pages}
    return render(request, 'shop.html', context)



