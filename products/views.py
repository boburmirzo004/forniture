from django.shortcuts import render


def checkout_page_view(request):
    return render(request, 'products/checkout.html')


def cart_page_view(request):
    return render(request, 'products/cart.html')


def product_detail_page_view(request):
    return render(request, 'products/product-detail.html')


def product_list_page_view(request):
    return render(request, 'products/products-list.html')


def wishlist_page_view(request):
    return render(request, 'products/wishlist.html')
