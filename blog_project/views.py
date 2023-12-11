from django.shortcuts import render
from posts.models import Post
from category.models import Category

def index(req, category_slug = None) :
    data = Post.objects.all()
    if category_slug is not None :
        cate = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=cate)
    
    category = Category.objects.all()
    return render(req, 'index.html', {'data' : data, 'category' : category})