from django.shortcuts import render
from posts.models import Post


def index(request):
    queried = Post.objects.all()
    print(queried)
    return render(request, 'index.html', context={'posts':queried})