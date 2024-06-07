from django.urls import path, include
from django.contrib import admin

import app_api_books
from app_api_books import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include(app_api_books.urls), name= 'books'),
]

