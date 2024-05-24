from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Books
from .serializer import BooksSerializer


# Create your views here.

@api_view(['GET'])
def book_list(request):
   if request.method == 'GET':
        books = Books.objects.all()

        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

  #  return HttpResponse(status=status.HTTP_404_NOT_FOUND)