from django.shortcuts import render


def account_page_view(request):
    return render(request, 'users/account.html')


def register_page_view(request):
    return render(request, 'users/register.html')


def login_page_view(request):
    return render(request, 'users/login.html')


def reset_password_page_view(request):
    return render(request, 'users/reset-password.html')
