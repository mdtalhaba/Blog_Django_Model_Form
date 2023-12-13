from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from posts.forms import PostForm
from posts.models import Post
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


# Add Post Using Function View
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

# Add Post Using Class View
@method_decorator(login_required(login_url="/author/login/"), name='dispatch')
class AddPostCreateView(CreateView) :
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# Edit Post Using Function View
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

# Edit Post Using Class View
@method_decorator(login_required(login_url="/author/login/"), name='dispatch')
class EditPostView(UpdateView) :
    model = Post
    form_class = PostForm
    template_name = 'posts/add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

# Delete Post Using Function View
@login_required(login_url="/author/login/")
def delete_post(req, id) :
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')


# Delete Post Using Class View
@method_decorator(login_required(login_url="/author/login/"), name='dispatch')
class DeletePostView(DeleteView) :
    model = Post
    template_name = 'posts/delete_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


class DetailsPostView(DetailView) :
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'posts/details_post.html'
