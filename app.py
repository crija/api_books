# Criando uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# Install Flask
# Import flask, jsonify to convert python values to djon
# Inicializar o flask

from flask import Flask, jsonify, request

app = Flask(__name__)

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

# Consult all
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Consult id
@app.route('/books/<int:id>', methods=['GET'])
def get_book_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

# Edit information
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_ad(id):
    # guardar em uma variável as informações que foram enviadas do user to the api
    altered_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(altered_book)
            return jsonify(book)

# Create book
@app.route('/books', methods=['POST'])
def create_new_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# Delite book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
    return jsonify(books)

# Inicialize application
app.run(port=5000,host='localhost',debug=True)