from django.urls import path
from todo import views

app_name = 'todo'
urlpatterns = [
    path('todo/', views.todo_list_view, name='todo_list_view'),
    path('todo/add/', views.todo_list_edit, name='todo_add'),
    path('todo/mod/<int:todo_id>/', views.todo_list_edit, name='todo_edit'),
    path('todo/del/<int:todo_id>/', views.todo_list_delete, name='todo_del'),
]
