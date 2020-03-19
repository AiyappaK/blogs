from django.urls import path
from . import views
from .views import PostListView, PostDetailView , PostCreatelView ,PostUpdatelView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name = 'index'),
    path('about/', views.about, name = 'about'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'postDetail'),
    path('post/new/',PostCreatelView.as_view(), name = 'postCreate'),
    path('post/<int:pk>/update/',PostUpdatelView.as_view(), name = 'postUpdate'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'postDelete'),
    path('user/<str:username>/',UserPostListView.as_view(), name = 'userPost'),
]
