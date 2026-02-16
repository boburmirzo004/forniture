from django.urls import path

from shared.views import first_page_view, second_page_view, third_page_view, fourth_page_view, fifth_page_view, \
    sixth_page_view, seventh_page_view, eighth_page_view, ninth_page_view, tenth_page_view, eleventh_page_view, \
    twelfth_page_view, thirteenth_page_view, fourteenth_page_view

app_name = 'shared'

urlpatterns = [
    path('', first_page_view, name='home'),
    path('account/', second_page_view, name='account'),
    path('blog-detail/', third_page_view, name='blog-detail'),
    path('blog-list/', fourth_page_view, name='blog-list'),
    path('cart/', fifth_page_view, name='cart'),
    path('checkout/', sixth_page_view, name='checkout'),
    path('contact/', seventh_page_view, name='contact'),
    path('about-us/', eighth_page_view, name='about-us'),
    path('login/', ninth_page_view, name='login'),
    path('product-detail/', tenth_page_view, name='product-detail'),
    path('product-list/', eleventh_page_view, name='product-list'),
    path('register/', twelfth_page_view, name='register'),
    path('reset-password/', thirteenth_page_view, name='reset-password'),
    path('wishlist/', fourteenth_page_view, name='wishlist'),
]
