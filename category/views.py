from django.shortcuts import render, redirect
from category.forms import CategoryForm

def add_category(req) :
    if req.method == 'POST' :
        category_form = CategoryForm(req.POST)
        if category_form.is_valid() :
            category_form.save()
            return redirect('add_category')
        
    category_form = CategoryForm()
    return render(req, 'category/add_category.html', {'form' : category_form})
