from django.urls import path
from . import views
from .views import TasksView as tasks, TaskView as task
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    # path('tasks/list', views.tasksList, name="tasksList"),
    # path('task/<str:pk>', views.taskDetails, name="task-details"),
    # path('task/create/', views.taskCreate, name="taskCreate"),
    # path('task/<str:pk>/update/', views.taskUpdate, name="taskUpdate"),
    # path('task2/create/', views.task2Create, name="taskCreate"),
    path('tasks', tasks.as_view()),
    path('task/<int:pk>', task.as_view(), name="get-task-by-id"),
]