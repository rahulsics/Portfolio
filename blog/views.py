from django.shortcuts import render
from.models import blog

def all_blogs(request):
    blogs = blog.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blog.html', {'blogs':blogs})
