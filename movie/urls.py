from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/edit/', views.edit, name="edit"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('<int:id>/scores/new/', views.score_new, name="score_new"),
    path('<int:id>/scores/<int:s_id>/delete/', views.score_delete, name="score_delete"),
    ]