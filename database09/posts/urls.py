from django.urls import path
from .views import post_create_view, main_view

app_name='posts'
urlpatterns = [
    path('new/',post_create_view,name='post_create_view'),
    path('main/',main_view,name='main'),
]