from django.urls import path

from . import views
from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = "blog"
urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("contact/", views.contact, name="blog-contact"),
    path("posts/", PostListView.as_view(), name="blog-posts"),
    path("post_detail/<int:pk>/", PostDetailView.as_view(), name="post-details"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
