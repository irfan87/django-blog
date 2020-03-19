from django.urls import path
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
)

from . import views

urlpatterns = [
	path('', PostListView.as_view(), name='post-home'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('post/<str:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<str:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
	path('post/<str:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name='contact'),
]