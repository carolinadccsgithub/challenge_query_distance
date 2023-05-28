from django.urls import path
from .views import index, historical

urlpatterns = [
    path('', index, name='index'),
       path('historical', historical, name='historical'),
]