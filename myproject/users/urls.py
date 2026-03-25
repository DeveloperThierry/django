from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
    path("", views.usershome, name="usershome"),
    path("users_list/", views.users_list, name="users_list"),
    path("register/", views.register_view, name="register_user")
    
]
