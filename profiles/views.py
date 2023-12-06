from django.shortcuts import render, redirect
from profiles.forms import ProfileForm

def add_profile(req) :
    if req.method == 'POST' :
        profile_form = ProfileForm(req.POST)
        if profile_form.is_valid() :
            profile_form.save()
            return redirect('add_profile')
        
    profile_form = ProfileForm()
    return render(req, 'profiles/add_profile.html', {'form' : profile_form})
