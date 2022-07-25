from django.views import generic
from .models import Post
from .forms import CommentForm, PostForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required


# ALL BLOGS
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog_posts.html'
    paginate_by = 4


# INDIVIDUAL BLOG POST DETAILS (COMMENTS)
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def post_detail(request, slug):
    """ a view to see the individual blog post with potential to add a comment """
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request , template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


# FUTURE FEATURE PREFERENCES - ADD A BLOG
# @login_required
# def add_post(request):
#     """ a view to add a post to the blog """

#     if request.method == "POST":
#         form = PostForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             author = request.user
#             obj.author = author
#             obj.save()

#             messages.success(request, "Successfully added your blog post")
#             return redirect(reverse('post_detail', args=[obj.slug]))
#         else:
#             messages.error(
#                 request, "Failed to add blog post, please check the form is \
#                     valid")
#     else:
#         form = PostForm()

#     template = 'blog/add_post.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)