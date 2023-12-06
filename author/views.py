from django.shortcuts import render, redirect
from author.forms import AuthorForm

def add_author(req) :
    if req.method == 'POST' :
        author_form = AuthorForm(req.POST)
        if author_form.is_valid() :
            author_form.save()
            return redirect('add_author')
        
    author_form = AuthorForm()
    return render(req, 'author/add_author.html', {'form' : author_form})
