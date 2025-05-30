from django.urls import path
from .views import IndexView, CreateView, DetailView, EditPostView, delete_view, PostAPI, CommentAPI, start_chat_with_owner, find_similar_posts

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateView.as_view(), name='create'),
    path('detail/<int:post_id>/', DetailView.as_view(), name='detail'),
    path('edit_post/<int:post_id>/', EditPostView.as_view(), name='edit_post'),
    path('delete/<int:post_id>/', delete_view, name='post_delete'),
    path('edit_post/success/<int:post_id>/', EditPostView.as_view(), name='edit_post_success'),
    path('post_api/', PostAPI.as_view(), name='post_api'),
    path('comment_api/<int:post_id>/', CommentAPI.as_view(), name='comment_api'),
    path('start/<int:post_id>/', start_chat_with_owner, name='start_chat_with_owner'),
    # Add this to your urlpatterns
    path('find-similar/<int:post_id>/', find_similar_posts, name='find_similar_posts'),

]
