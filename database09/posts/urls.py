from django.urls import path
from .views import SearchFormView, post_create_view, main_view, post_detail_view, post_update_view

app_name='posts'
urlpatterns = [
    path('new/',post_create_view,name='post-create-view'),
    path('main/',main_view,name='main'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/edit/', post_update_view, name='post-update'),
    path('main/', SearchFormView.as_view(), name='search'),
]