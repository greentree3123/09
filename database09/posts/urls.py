from django.urls import path
from .views import post_create_view, main_view, post_list_view, SearchFormView, post_detail_view, post_update_view

app_name='posts'
urlpatterns = [
    path('new/',post_create_view,name='post-create-view'),
    path('main/',main_view,name='main'),
    path('main/',post_list_view,name='main'),
    path('main/', SearchFormView.as_view(), name='search'),
]