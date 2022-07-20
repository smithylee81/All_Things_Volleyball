from django.views import generic
from .models import Post

# from .forms import CommentForm, PostForm
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog_posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

