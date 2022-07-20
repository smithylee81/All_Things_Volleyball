from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
    # path('add_post/', views.add_post, name='add_post'),
    # path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    # path('delete/<slug:slug>/', views.delete_post, name='delete_post'), 