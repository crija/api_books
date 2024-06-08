from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.book_list, name= 'books'),
    path('create/', views.create_book, name= 'create'),
    path('<int:id>', views.delete_book, name= 'delete'),
    path('<int:id>', views.edit_book, name= 'edit'),
   
]


