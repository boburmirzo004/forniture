from django.urls import path

from blogs.views import blog_detail_page_view, blog_list_page_view

app_name='blogs'

urlpatterns =[
    path('blog-detail/', blog_detail_page_view, name='detail'),
    path('blog-list/', blog_list_page_view, name='list'),
]