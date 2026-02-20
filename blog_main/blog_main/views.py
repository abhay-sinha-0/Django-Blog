from django.shortcuts import render
from django.http import HttpResponse
from assignments.models import About
from blogs.models import Category,Blog

def home(request): 
    # categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    # print(featured_post)
    # print(categories)
    posts = Blog.objects.filter(is_featured=False, status='Published')
    # print(posts)
    
    # Fetch about us data
    try:
        about = About.objects.get()
    except:
        about=None
    
    context = {
        # 'categories': categories, 
        'featured_post': featured_post,
        'posts': posts,   
        'about': about,
    }
    return render(request, 'home.html', context)