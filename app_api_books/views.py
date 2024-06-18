# Buscar livros por título
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Books
from .serializer import BooksSerializer

# GET all books
@api_view(['GET', 'POST'])
def get_or_create_books(request):
   if request.method == 'GET':                          
      title = request.GET.get('title')
      author = request.GET.get('author')
      books = Books.objects.all()
      if title:
         books = books.filter(title=title)
      if author:
         books = books.filter(author=author)
      serializer = BooksSerializer(books, many=True)   
      return Response(serializer.data)
      
# POST book
   if request.method == 'POST':
      new_book = request.data
      serializer = BooksSerializer(data=new_book)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(status=status.HTTP_400_BAD_REQUEST)

# PUT book by id
@api_view(['PUT', 'DELETE', 'GET'])
def get_or_delete_or_put_book(request, id):
   if request.method == 'PUT':
      update_book = Books.objects.get(pk=id)
      serializer = BooksSerializer(update_book, data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(status=status.HTTP_202_ACCEPTED)

# DELETE book by id
   if request.method == 'DELETE':
      delete_book = Books.objects.get(pk=id)
      delete_book.delete()
      return Response(status=status.HTTP_202_ACCEPTED)

# GET book by id
   if request.method == 'GET':
      book = Books.objects.get(pk=id)
      serializer = BooksSerializer(book)
      return Response(serializer.data)

   return Response(status=status.HTTP_404_NOT_FOUND)





   
  