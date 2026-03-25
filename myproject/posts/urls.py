from django.urls import path
from . import views
app_name = "posts"
urlpatterns = [
    path("", views.homepage, name="posthome"),
    path("posts_list", views.posts_list, name="posts_list"),
    path("posts_list/<slug:slug>", views.post_page, name="post_page")
]