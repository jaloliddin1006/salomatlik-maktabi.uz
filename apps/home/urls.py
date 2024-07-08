from django.urls import path
from .views import HomePageView, ContactPage, MyFavouriteView, AddOrRemoveFavourite

app_name = "home"
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('my-favourite/', MyFavouriteView.as_view(), name='my-favourite'),
    path('api/add-or-remove-favourite/', AddOrRemoveFavourite.as_view(), name='add-or-remove-favourite'),
]
