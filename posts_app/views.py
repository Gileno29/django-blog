from django.shortcuts import render
from posts_app.models import Posts
# Create your views here.

def post_list(request):
    template_name = 'post-list.html'
    posts= Posts.objects.all()
    context ={
        'posts': posts
    }
    return render(request,template_name, context)


def post_create(request):
    pass

def post_detail(request):
    template_name='post-detail.html'