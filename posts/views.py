from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.decorators import login_required

@login_required(login_url="/author/login/")
def add_post(req) :
    if req.method == 'POST' :
        post_form = PostForm(req.POST)
        if post_form.is_valid() :
            post_form.instance.author = req.user
            post_form.save()
            return redirect('add_post')
        
    post_form = PostForm()
    return render(req, 'posts/add_post.html', {'form' : post_form})

@login_required(login_url="/author/login/")
def edit_post(req, id) :
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if req.method == 'POST' :
        post_form = PostForm(req.POST, instance=post)
        if post_form.is_valid() :
            post_form.instance.author = req.user
            post_form.save()
            return redirect('home')
        
    return render(req, 'posts/add_post.html', {'form' : post_form})

@login_required(login_url="/author/login/")
def delete_post(req, id) :
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')
