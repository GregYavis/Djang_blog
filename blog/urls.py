from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, \
    PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    # localhost:8000\blog\''
    path('about/', views.about, name='blog-about'),
    # localhost:8000\blog\'about'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post-delete'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),

]
