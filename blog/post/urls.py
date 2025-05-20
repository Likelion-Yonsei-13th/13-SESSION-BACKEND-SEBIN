from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/update/',views.update_post, name='update_post'),
    path('<int:post_id>/delete/', views.delete_post, name = 'delete_post'),
    path('<int:post_id>/comment/', views.comment_list, name='comment_list'),
    path('<int:post_id>/comment/create/', views.create_comment, name="create_comment"),
    path('<int:comment_id>/update/', views.update_comment, name="update_comment"),
    path('<int:comment_id>/delete/', views.delete_comment, name="delete_comment"),
]