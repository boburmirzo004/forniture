from django.shortcuts import render


def first_page_view(request):
    return render(request, 'home.html')


def second_page_view(request):
    return render(request, 'account.html')


def third_page_view(request):
    return render(request, 'blog-detail.html')


def fourth_page_view(request):
    return render(request, 'blogs-list.html')


def fifth_page_view(request):
    return render(request, 'cart.html')


def sixth_page_view(request):
    return render(request, 'checkout.html')


def seventh_page_view(request):
    return render(request, 'contact.html')


def eighth_page_view(request):
    return render(request, 'about-us.html')


def ninth_page_view(request):
    return render(request, 'login.html')


def tenth_page_view(request):
    return render(request, 'product-detail.html')


def eleventh_page_view(request):
    return render(request, 'product-list.html')


def twelfth_page_view(request):
    return render(request, 'register.html')


def thirteenth_page_view(request):
    return render(request, 'reset-password.html')


def fourteenth_page_view(request):
    return render(request, 'wishlist.html')
