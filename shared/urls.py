from django.urls import path

from shared.views import home_page_view, contact_page_view, about_us_page_view

app_name = 'shared'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_page_view, name='contact'),
    path('about-us/', about_us_page_view, name='about'),


]


# path('account/', account_page_view, name='account'),
# path('login/', login_page_view, name='login'),
#
# path('register/', register_page_view, name='register'),
# path('reset-password/', reset_password_page_view, name='reset-password'),