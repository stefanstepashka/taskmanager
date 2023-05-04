from django.urls import path, include
from . import views
from . import api
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tasks', api.TaskViewSet)


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('api/', include(router.urls))
]