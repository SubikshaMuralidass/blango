from django.urls import path
from . import views

app_name = 'picture'

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('grid/', views.gallery_grid, name='gallery_grid'),
    path('event/<int:event_id>/images/', views.event_images, name='event_images'),
]
