from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog_posts/', views.PostList.as_view(), name='blog_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]
    
    #path('add_post/', views.add_post, name='add_post'),
    # path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    # path('delete/<slug:slug>/', views.delete_post, name='delete_post'), 