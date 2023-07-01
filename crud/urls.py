from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('add', add, name='add'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
    path('deletePlayers', deletePlayers, name='deletePlayers'),
]
