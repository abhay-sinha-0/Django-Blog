from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # category crud
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_categories, name='add_categories'),
    path('categories/edit/<int:pk>/', views.edit_categories, name='edit_categories'),
    path('categories/delete/<int:pk>/', views.delete_categories, name='delete_categories'),
    
    # blog post crud
    path('posts/', views.posts, name='posts'),
    path('posts/add_post/', views.add_post, name='add_post'),
    path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
]
