from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

app_name = "users"

urlpatterns = [
    path('', views.login_view,name='login'),
    path('signup/', views.signup_view, name='signup'),
]
