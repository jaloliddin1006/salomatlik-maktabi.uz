from django.urls import path
from .views import FormulaPage, FormulaDetail, CalculateAPI

app_name = "formula"
urlpatterns = [
    path('', FormulaPage.as_view(), name='formula'),
    path('<int:pk>/', FormulaDetail.as_view(), name='detail'),
    path('api/<int:id>/', CalculateAPI.as_view(), name='calculate-api'),
    
]