from django.shortcuts import render


def blog_detail_page_view(request):
    return render(request, 'blogs/blog-detail.html')


def blog_list_page_view(request):
    return render(request, 'blogs/blogs-list.html')
