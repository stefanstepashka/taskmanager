from django.urls import path, include
from . import views
from . import api
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import register_view
router = DefaultRouter()
router.register(r'tasks', api.TaskViewSet)


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:task_id>/', views.task_update, name='task_update'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('api/', include(router.urls)),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]