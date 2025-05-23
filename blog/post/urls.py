from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view(), name='create_post'),
    path('<int:post_id>/', PostDetailView.as_view(), name="detail_post")
]