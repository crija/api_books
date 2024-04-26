from flask import Blueprint, render_template

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
   pass

# Update book
@books_route.route('/<int:book_id>/update', methods=['PUT'])
def update_book(book_id):
   pass

# Delete book
@books_route.route('/<int:book_id>/delete', methods=['DELETE'])
def delete_book(book_id):
   pass