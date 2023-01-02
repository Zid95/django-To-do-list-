from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('clear_todos', views.clear_all, name='clear_all'),
    path('<int:id>/update', views.update_todo, name='update')
]
