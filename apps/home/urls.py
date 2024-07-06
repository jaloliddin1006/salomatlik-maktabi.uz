from django.urls import path
from .views import HomePageView, ContactPage, FormulaPage

app_name = "home"
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('formula/', FormulaPage.as_view(), name='formula'),
]
