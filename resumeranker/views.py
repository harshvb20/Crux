from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {"posts": posts}
        return render(request, "home.html", context)
