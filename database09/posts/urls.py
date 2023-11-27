from django.urls import path
from .views import post_create_view

app_name='posts'
urlpatterns = [
    path('new/',post_create_view,name='post-create'),
]