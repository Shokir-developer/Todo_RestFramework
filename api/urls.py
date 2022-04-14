from django.urls import path
from .views import indexApi, add, detail

urlpatterns = [

    path('', indexApi, name='api'),
    path('add/', add),
    path('<str:pk>/', detail),
]
