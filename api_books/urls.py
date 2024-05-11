from django.urls import path
from app_api_books import views

urlpatterns = [
    path('',views.book_list, name='book_list'),
]
