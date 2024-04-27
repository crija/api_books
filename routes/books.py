from flask import Blueprint, request, jsonify

books_route = Blueprint('books', __name__)

books = [
    {
        "id": 1,
        "title": "A máquina do caos",
        "author": "Max Fisher"
    },
    {
        "id": 2,
        "title": "A estrada do futuro",
        "author": "Bill Gates"
    },
    {
        "id": 3,
        "title": "Terra Americana",
        "author": "Jeanine Cummins"
    }
]

# List books
@books_route.route('/')
def book_list():
   return books

# Create book
@books_route.route('/', methods=['POST'] )
def add_book():
   return '', 201

# Id book
@books_route.route('/<int:book_id>')
def get_book(book_id):
   for book in books:
        if book.get('id') == book_id:
            return book

# Update book
@books_route.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    altered_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == book_id:
            books[index].update(altered_book)
            return book

# Delete book
@books_route.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book.get('id') == book_id:
            del books[index]
    return books