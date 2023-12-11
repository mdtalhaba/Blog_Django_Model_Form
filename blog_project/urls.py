from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('category/<slug:category_slug>', views.index, name='category_slug'),
    path('author/', include('author.urls')),
    path('category/', include('category.urls')),
    path('post/', include('posts.urls')),
]
