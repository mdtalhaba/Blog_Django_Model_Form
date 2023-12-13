from django.urls import path
from author.views import register, user_login, user_logout, profile, pass_change, edit_profile, UserLoginView, UserLogoutView, UserRegisterView

urlpatterns = [
    # path('register/', register, name='register'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', user_login, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', user_logout, name='logout'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', pass_change, name='pass_change'),
]
