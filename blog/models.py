from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

# BLOG POST MODEL

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

# BLOG DELETE MODEL
# @receiver(post_delete, sender=Post)
# def submission_delete(sender, instance, **kwargs):
#     instance.image.delete(False)


# def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(
#             instance.author.username + "-" + instance.title)

# pre_save.connect(pre_save_blog_post_receiver, sender=Post)


# BLOG COMMENTS MODEL
# class Comment(models.Model):
#     post = models.ForeignKey(
#         Post, related_name='comments', on_delete=models.CASCADE)
#     comment_author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="comment", default=1)
#     comment = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)