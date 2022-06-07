from django.urls import path
from posts.views import PostsListView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('', PostsListView.as_view(), name="list"),
    path('<int:pk>/', PostDetailView.as_view(), name="detail"),
]
