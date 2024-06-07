from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Books
from .serializer import BooksSerializer


# Create your views here.

#List books
@api_view(['GET'])
def book_list(request):
   if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

   return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#creating book - POST
@api_view(['POST'])
def create_book(request):
   if request.method == 'POST':
      new_book = request.data
      serializer = BooksSerializer(data=new_book)

      if serializer.is_valid(raise_exception=True):
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(status=status.HTTP_400_BAD_REQUEST)
