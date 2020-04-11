from django.shortcuts import render
from .models import Post

# Create your views here.
posts = [
    {
        'author': "kc",
        'title': "First Post",
        'content': "post Content",
        'date_posted': 'April 11, 2020'
    },
    {
        'author': "kc",
        'title': "First Post",
        'content': "post Content",
        'date_posted': 'April 11, 2020'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html",context)

def about(request):
    return render(request, "blog/about.html")
