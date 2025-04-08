from django.urls import path
from . import views

urlpatterns = [
    path('photo/upload/', views.photo_upload, name='photo_upload'),
    path('photo/<int:photo_id>/', views.view_photo, name='view_photo'),
    path('photo/<int:photo_id>/edit/', views.edit_photo, name='edit_photo'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('blog/<int:blog_id>/edit/', views.edit_blog, name='edit_blog'),

    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/users/', views.admin_users, name='admin_users'),
    path('admin-panel/users/delete/<int:user_id>/', views.admin_delete_user, name='admin_delete_user'),
    path('admin-panel/photos/', views.admin_photos, name='admin_photos'),
    path('admin-panel/photos/delete/<int:photo_id>/', views.admin_delete_photo, name='admin_delete_photo'),
    path('admin-panel/blogs/', views.admin_blogs, name='admin_blogs'),
    path('admin-panel/blogs/delete/<int:blog_id>/', views.admin_delete_blog, name='admin_delete_blog'),
    path('admin-panel/categories/', views.admin_categories, name='admin_categories'),
    path('admin-panel/categories/add/', views.admin_add_category, name='admin_add_category'),
    path('admin-panel/categories/edit/<int:cat_id>/', views.admin_edit_category, name='admin_edit_category'),
    path('admin-panel/categories/delete/<int:cat_id>/', views.admin_delete_category, name='admin_delete_category'),
    path('blog/create/', views.blog_and_photo_upload, name='blog_and_photo_upload'),

]
