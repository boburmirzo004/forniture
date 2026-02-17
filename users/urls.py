from django.urls import path

from users.views import account_page_view, register_page_view, login_page_view, reset_password_page_view

app_name = 'users'

urlpatterns = [
    path('account/', account_page_view, name='account'),
    path('register/', register_page_view, name='register'),
    path('login/', login_page_view, name='login'),
    path('reset-password/', reset_password_page_view, name='reset-password'),

]
