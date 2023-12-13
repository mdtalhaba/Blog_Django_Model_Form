from django.db import models
from category.models import Category
from django.contrib.auth.models import User

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/media/uploads/', blank=True, null=True)

    def __str__(self) :
        return self.title
    

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Comment by {self.name}"
