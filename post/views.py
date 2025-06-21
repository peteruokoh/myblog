from django.shortcuts import render, redirect
from django.http import HttpResponse
from post.models import Post
from .forms import PostForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def postlist(request):
    posts = Post.objects.all().order_by("-publishDate")
    return render(request, "feedlist.html", {"posts": posts}) # {"posts": posts} is used to pass data to the template

def create_post(request):
    if (request.method == "POST"):
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.publishDate = datetime.today()
            form.save()
            return redirect("postlist")
    else:
        # for GET request
        form = PostForm()
        return render(request, "create_post.html", {"form": form})
    
def edit_post(request, id):
    post = Post.objects.get(id=id)
    if (request.method == "POST"):
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            post = form.save(commit=False)
            post.publishDate = datetime.today()
            form.save()
            return redirect("postlist")
    else:
        # for GET request
        form = PostForm(instance = post)
        return render(request, "create_post.html", {"form": form})
    
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("postlist")