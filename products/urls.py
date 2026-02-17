from django.urls import path

from products.views import cart_page_view, checkout_page_view, product_detail_page_view, product_list_page_view, \
    wishlist_page_view

app_name ='products'

urlpatterns = [
    path('checkout/', checkout_page_view, name='checkout'),
    path('cart/', cart_page_view, name='cart'),
    path('product-detail/', product_detail_page_view, name='detail'),
    path('product-list/', product_list_page_view, name='list'),
    path('wishlist/', wishlist_page_view, name='wishlist'),
]
