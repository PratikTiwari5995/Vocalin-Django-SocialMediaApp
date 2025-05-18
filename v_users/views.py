from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def profile_view(request):
    profile = request.user.profile 
    return render(request, 'v_users/profile.html', {'profile': profile})


def profile_edit_view(request):
    form = EditPofileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = EditPofileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Edited")
            return redirect('profile_page')
        
    return render(request, 'v_users/profile_edit.html', {'form': form})
