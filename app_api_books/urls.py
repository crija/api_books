from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.list_and_criate_books, name= 'books'),
    path('/<int:id>', views.update_book, name= 'update_book'),

]


