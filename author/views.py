from django.shortcuts import render, redirect
from author.forms import RegistrationForm, ChangeUserForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post


def register(req) :
    if req.method == 'POST' :
        register_form = RegistrationForm(req.POST)
        if register_form.is_valid() :
            messages.success(req, 'Registration Successfull')
            register_form.save()
            return redirect('register')
    else : 
        register_form = RegistrationForm()
    return render(req, 'author/register.html', {'form' : register_form, 'type' : 'Register'})


def user_login(req) :
    if req.method == 'POST' :
        login_form = AuthenticationForm(req, req.POST)
        if login_form.is_valid() :
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None :
                messages.success(req, 'Log In Successfull')
                login(req, user)
                return redirect('profile')
            else :
                messages.warning(req, 'Log In Information is Incorrenct')
                return redirect('register')
    else :
        login_form = AuthenticationForm()
    return render(req, 'author/register.html', {'form': login_form, 'type' : 'Login'})


def user_logout(req) :
    logout(req)
    return redirect('login')


@login_required(login_url="/author/login/")
def profile(req) :
    data = Post.objects.filter(author = req.user)
    return render(req, 'author/profile.html', {'data' : data })


@login_required(login_url="/author/login/")
def edit_profile(req) :
    if req.method == 'POST' :
        profile_form = ChangeUserForm(req.POST, instance=req.user)
        if profile_form.is_valid() :
            messages.success(req, 'Your Information is Successfully Changed')
            profile_form.save()
            return redirect('profile')
    else : 
        profile_form = ChangeUserForm(instance=req.user)
    return render(req, 'author/edit_profile.html', {'form' : profile_form, 'type' : 'Update Profile'})



def pass_change(req) :
    if req.method == 'POST' :
        pass_change_form = PasswordChangeForm(req.user, data=req.POST)
        if pass_change_form.is_valid() :
            messages.success(req, 'Your Password is Successfully Changed')
            pass_change_form.save()
            update_session_auth_hash(req, pass_change_form.user)
            return redirect('profile')
    else : 
        pass_change_form = PasswordChangeForm(req.user)
    return render(req, 'author/pass_change.html', {'form' : pass_change_form, 'type' : 'Change Your Password'})