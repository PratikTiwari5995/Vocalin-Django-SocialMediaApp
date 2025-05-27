from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import Http404
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
# Create your views here.


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    return render(request, 'v_users/profile.html', {'profile': profile})


@login_required
def profile_edit_view(request):
    form = EditPofileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = EditPofileForm(request.POST, request.FILES,
                              instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Edited")
            return redirect('profile_page')
    return render(request, 'v_users/profile_edit.html', {'form': form})


@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "User Deleted")
        return redirect("home_page")
    return render(request, 'v_users/profile_delete.html')
