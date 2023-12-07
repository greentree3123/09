from django.urls import path
from .views import SearchFormView, post_create_view, main_view, post_detail_view, post_list_view, post_update_view, comment_delete_view, likes


app_name='posts'
urlpatterns = [
    path('new/',post_create_view,name='post-create-view'),
    path('main/',main_view,name='main'),
    path('<int:article_pk>/', post_detail_view, name='post-detail'),
    path('<int:article_pk>/edit/', post_update_view, name='post-update'),
    path('main/', SearchFormView.as_view(), name='search'),
    path('main/',post_list_view,name='main'),
    path('comment/<int:comment_id>/delete/', comment_delete_view, name='comment-delete'),
    path('<int:article_pk>/likes/', likes, name='likes'),
]