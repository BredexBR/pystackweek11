from django.urls import path
from . import views

urlpatterns = [
    path('sugestao/', views.sugestao, name="sugestao"),
]