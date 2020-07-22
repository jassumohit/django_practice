from . import views
from django.urls import path

app_name = "music"

urlpatterns = [
    path('', views.indexview.as_view(), name='index'),
    path('<int:pk>/', views.detailview.as_view(), name='detail'),
    path('<int:album_id>/favourite/', views.favourite, name='favourite'),
    path('album/add', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    path('register/',views.UserView.as_view(), name='register')
]