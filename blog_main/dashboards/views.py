from multiprocessing import context

from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, BlogPostsForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    
    context= {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/add_categories.html', context)

def edit_categories(request, pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form':form,
        'category': category,
    }
    return render(request,'dashboard/edit_categories.html', context)

def delete_categories(request,pk):
    category=get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'dashboard/posts.html', context)  

def add_post(request):
    if request.method == "POST":
        form = BlogPostsForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # Temporarily save the form data without committing to the database
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id) # Generate slug using the title and the post ID
            # post.save()  # Save the post with the generated slug
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)
    form = BlogPostsForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/add_post.html',context)

def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostsForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(post.title) + '-' + str(post.id) # Update slug using the title and the post ID
            post.save()  # Save the post with the updated slug
            return redirect('posts')
    form = BlogPostsForm(instance=post)
    context={
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html',context)


def delete_post(request,pk):
    post=get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            # print('form is invalid')
            print(form.errors)
    form = AddUserForm()
    context = {
        'form': form,       
    }
    return render(request, 'dashboard/add_user.html',context)

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = EditUserForm(instance=user)
    # form = AddUserForm()
    
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')