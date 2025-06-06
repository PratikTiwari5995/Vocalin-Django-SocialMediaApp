"""
URL configuration for Vocalin_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from v_post.views import *
from v_users.views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home_page'),
    path('category/<str:tag>', home_view, name='category_page'),
    path('post/create', post_create_view, name='create_post'),
    path('post/delete/<str:pk>/', post_delete_view, name='delete_post'),
    path('post/edit/<str:pk>/', post_edit_view, name='edit_post'),
    path('post/<str:pk>/', post_page_view, name='post_page'),
    path('post/<str:pk>/like', post_like_view, name='post_like'),
    path('profile/', profile_view, name='profile_page'),
    path('profile/edit/', profile_edit_view, name='edit_profile'),
    path('profile/delete', profile_delete_view, name='profile_delete'),
    path('commentsend/<pk>', comment_send, name='comment_send'),
    path('comment/delete/<pk>', comment_delete_view, name='comment_delete'),
    path('replysend/<pk>', reply_send, name='reply_send'),
    path('reply/delete/<pk>', reply_delete_view, name='reply_delete')
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
