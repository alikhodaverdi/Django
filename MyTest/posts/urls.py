
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view()) ,
    path('<int:post_id>/',PostDetailView.as_view())
]
