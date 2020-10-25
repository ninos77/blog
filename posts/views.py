from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "posts/posts.html", context)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, "posts/detail.html", context)


@login_required(login_url='home')
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('detail', kwargs={'id': post.id}))
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, "posts/create.html", context)
