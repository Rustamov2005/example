from django.shortcuts import render
from django.views import View
from products.models import Product
from .helpers import Paginator


class PostListView(View):

    def blog(self, request):
        products = Product.get_queryset()
        page = int(request.GET.get('page', 1))
        pages = Paginator.page_pagination(products, 6, page)
        context = {'pages': pages, 'page': page, "previous_page": page - 1, "next_page": page + 1, "products": pages}
        return render(request, 'blog.html', context)

