from django.urls import path
from . import views

app_name = 'resources'
urlpatterns = [
    path('', views.ResourceListView.as_view(), name='resource-list'),
    path('<str:slug>/', views.ResourceDetailView.as_view(), name='resource-detail'),
     path('api/resource/<int:pk>/watermarked/', views.WatermarkedFileView.as_view(), name='watermarked-file'),
     path('api/resource/<int:pk>/download/', views.DownloadFileView.as_view(), name='download-file'),
]
