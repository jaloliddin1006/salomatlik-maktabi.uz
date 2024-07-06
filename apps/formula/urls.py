from django.urls import path
from .views import FormulaPage, FormulaDetail

app_name = "formula"
urlpatterns = [
    path('', FormulaPage.as_view(), name='formula'),
    path('<int:pk>/', FormulaDetail.as_view(), name='detail'),
    
]