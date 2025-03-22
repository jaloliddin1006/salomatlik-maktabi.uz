from django.urls import path
from . import views


app_name = 'resources'
urlpatterns = [
    path('', views.ResourceListView.as_view(), name='resource-list'),
    path('<str:slug>/', views.ResourceDetailView.as_view(), name='resource-detail'),
    path('api/resource/<int:pk>/watermarked/', views.WatermarkedFileView.as_view(), name='watermarked-file'),
    path('api/resource/<int:pk>/download/', views.DownloadFileView.as_view(), name='download-file'),
    path('home_resourses/', views.HomePageView.as_view(), name='home_resourse'),
    # path('category_resources/<int:id>/', views.CategoryRecoursesView.as_view(), name='category_resurslari'),
    # path('resource_type/<int:id>/', views.ResourceTypeResourcesView.as_view(), name='resource-type')
       
]

from django.conf.urls import handler404
from .views import custom_404_view

handler404 = custom_404_view