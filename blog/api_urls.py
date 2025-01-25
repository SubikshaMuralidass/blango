from django.urls import path
#from . import api_views
from blog.api_views import post_list, post_detail

"""urlpatterns = [
    path('posts/', api_views.post_list, name='api_post_list'),
    path('posts/<int:pk>/', api_views.post_detail, name='api_post_detail'),
]
"""
urlpatterns = [
    path('posts/',post_list, name='api_post_list'),
    path('posts/<int:pk>/', post_detail, name='api_post_detail'),
]