from django.urls import path
from crud import views

urlpatterns = [
   path('members/', views.index, name='index'),
   path('members/add/', views.edit, name='add'),
   path('members/edit/(?P<id>\d+)/', views.edit, name='edit'),
   path('members/delete/(?P<id>\d+)/', views.delete, name='delete'),
   path('members/', views.detail, name='detail'),
]
