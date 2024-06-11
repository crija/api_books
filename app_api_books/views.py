from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Books
from .serializer import BooksSerializer

# Create your views here.

# List books - GET

@api_view(['GET', 'POST'])
def list_and_criate_books(request):

   if request.method == 'GET':
      books = Books.objects.all()
      serializer = BooksSerializer(books, many=True)
      return Response(serializer.data)

# Creating book - POST

   if request.method == 'POST':
      new_book = request.data
      serializer = BooksSerializer(data=new_book)

      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit book - PUT

@api_view(['PUT', 'DELETE'])
def update_book(request, id):
   if request.method == 'PUT':
      update_book = Books.objects.get(pk=id)

      serializer = BooksSerializer(update_book, data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response(status=status.HTTP_202_ACCEPTED)
      
# Delete books - DELETE

   if request.method == 'DELETE':
      delete_book = Books.objects.get(pk=id)
      delete_book.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
   
   return Response(status=status.HTTP_400_BAD_REQUEST)
