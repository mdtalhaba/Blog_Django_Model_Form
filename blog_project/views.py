from django.shortcuts import render
from posts.models import Post

def index(req) :
    data = Post.objects.all()
    return render(req, 'index.html', {'data' : data})