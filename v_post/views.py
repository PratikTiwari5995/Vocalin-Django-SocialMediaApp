from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

# Create your views here.


def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()

    categories = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tag': tag
    }
    return render(request, 'v_post/home.html', context)


@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostCreateForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post Created")
            return redirect('home_page')
    else:
        form = PostCreateForms()
    return render(request, 'v_post/post_create.html', {'form': form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post Deleted")
        return redirect('home_page')

    return render(request, 'v_post/post_delete.html', {'post': post})


@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Edited')
            return redirect('home_page')

    else:
        form = EditPostForm(instance=post)
    return render(request, 'v_post/post_edit.html', {'post': post, 'form': form})


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'v_post/post_page.html', {'post': post})
