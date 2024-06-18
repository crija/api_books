from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.get_or_create_books, name= 'books'),
    path('/<int:id>', views.get_or_delete_or_put_book, name= 'update_book'),

]


