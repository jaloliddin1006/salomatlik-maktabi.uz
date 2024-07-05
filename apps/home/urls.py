from django.urls import path
from .views import HomePageView, ContactPage

app_name = "home"
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
