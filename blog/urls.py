from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('article/<int:article_id>', views.article_page),
    path('edit/<int:article_id>', views.edit_article_page),
    path('edit_action', views.edit_action),
]
