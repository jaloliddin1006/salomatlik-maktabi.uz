from django.urls import path
from . import views

app_name = 'resources'
urlpatterns = [
    path('', views.ResourceListView.as_view(), name='resource-list'),
    path('<str:slug>/', views.ResourceDetailView.as_view(), name='resource-detail'),
]
