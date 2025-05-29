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
    commentForm = CommentCreateForm(request.POST)
    replyForm = ReplyCreateForm(request.POST)
    context = {
        'post': post,
        'commentForm': commentForm,
        'replyForm': replyForm
    }
    return render(request, 'v_post/post_page.html', context)


@login_required
def comment_send(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return redirect('post_page', pk=post.id)


@login_required
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comments, id=pk, author=request.user)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment Deleted")
        return redirect('post_page', comment.parent_post.id)

    return render(request, 'v_post/comment_delete.html', {'comment': comment})


@login_required
def reply_send(request, pk):
    comment = get_object_or_404(Comments, id=pk)

    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.parent_comment = comment
            reply.save()

    return redirect('post_page', pk=comment.parent_post.id)


def reply_delete_view(request, pk):
    reply = get_object_or_404(Reply, id=pk, author=request.user)
    if request.method == 'POST':
        reply.delete()
        messages.success(request, "reply Deleted")
        return redirect('post_page', reply.parent_comment.parent_post.id)

    return render(request, 'v_post/reply_delete.html', {'reply': reply})
