"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path, include

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
    path('photo-feed/', blog.views.photo_feed, name='photo_feed'),
    path('blog-feed/', blog.views.blog_feed, name='blog_feed'),

    path('', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),

    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/Cmdp.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/CmdpA.html'),
         name='password_change_done'
         ),

    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    path('blog/create', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', blog.views.view_blog, name='view_blog'),
    path('photo/upload-multiple/', blog.views.create_multiple_photos, name='create_multiple_photos'),
    path('follow-users/', blog.views.follow_users, name='follow_users'),
    path('about-us/', blog.views.about, name='about'),
    path('contact-us/', blog.views.contact, name='contact'),
    path('confirmation/', blog.views.confirmation, name='confirmation'),
    path('auth/', include('authentication.urls')),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#  les images stockées dans le répertoire MEDIA_ROOT seront servies au chemin donné par MEDIA_URL.