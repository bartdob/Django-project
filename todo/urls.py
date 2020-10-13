from django.urls import path
from . import views
# from todo.views import addTodo
# from .views import TodoDetailView, TodoCreateView, TodoListView

urlpatterns = [
    path('', views.todo, name='todo'),
    # path('', TodoListView.as_view(), name='todo'),
    path('addTodo/new/', views.addTodo, name='addTodo'),
    # path('', TodoCreateView.as_view(), name='todo-create'),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
    # path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]