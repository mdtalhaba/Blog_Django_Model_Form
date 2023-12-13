from django.shortcuts import render, redirect
from author.forms import RegistrationForm, ChangeUserForm, User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from posts.models import Post


# User Register Using Function View
def register(req) :
    if not req.user.is_authenticated :
        if req.method == 'POST' :
            register_form = RegistrationForm(req.POST)
            if register_form.is_valid() :
                messages.success(req, 'Registration Successfull')
                register_form.save()
                return redirect('register')
        else : 
            register_form = RegistrationForm()
        return render(req, 'author/register.html', {'form' : register_form, 'type' : 'Register'})
    else :
        return redirect('home')
    

# User Register Using Class View
class UserRegisterView(CreateView) :
    model = User
    form_class = RegistrationForm
    template_name = 'author/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration Successfull')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context


# User Login Using Function View
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


# User Login Using Class View
class UserLoginView(LoginView) :
    template_name = 'author/register.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Log In Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Log In Information is Incorrenct')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Log In'
        return context
    
    


# User Logout Using Function View
def user_logout(req) :
    logout(req)
    return redirect('login')

# User Logout Using Class View
@method_decorator(login_required(login_url="/author/login/"), name='dispatch')
class UserLogoutView(LogoutView) :    
    def get_success_url(self):
        return reverse_lazy('login')


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