# Buscar livros por título



from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Books
from .serializer import BooksSerializer

@api_view(['GET', 'POST'])
def list_and_criate_books(request):
   if request.method == 'GET':
      books = Books.objects.all()
      serializer = BooksSerializer(books, many=True)

      return Response(serializer.data)

   if request.method == 'POST':
      new_book = request.data
      serializer = BooksSerializer(data=new_book)
      if serializer.is_valid():
         serializer.save()

         return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
def update_book(request, id):
   if request.method == 'PUT':
      update_book = Books.objects.get(pk=id)
      serializer = BooksSerializer(update_book, data=request.data)

      if serializer.is_valid():
         serializer.save()

         return Response(status=status.HTTP_202_ACCEPTED)

   if request.method == 'DELETE':
      delete_book = Books.objects.get(pk=id)
      delete_book.delete()

      return Response(status=status.HTTP_202_ACCEPTED)

   if request.method == 'GET':
      book = Books.objects.get(pk=id)
      serializer = BooksSerializer(book)

      return Response(serializer.data)

   return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def book_title(request):
   if request.method == 'GET':                      
      if request.GET['title']:                            # Verifica se existe o parametro 'title' na url
         title_book = request.GET['title']                # Se o parametro existir, ele será guardado dentro da váriavel  'title_book'
         title = Books.objects.filter(title=title_book)   # Pegar o objeto no banco de dados e guardar dentro da variavel 'title'
         serializer = BooksSerializer(title, many=True)   # Transformar esse valor em json
         return Response(serializer.data)                 # Retornar os dados serializados

      else:
         return Response(status=status.HTTP_400_BAD_REQUEST) # Se a url vier com parametro errado, retorna o status code 400



   
  