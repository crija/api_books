import requests

def get_all_books():
    request = requests.get('http://localhost:5000/books')
    print(request)
    print(request.json())

def get_book_id(id):
    request = requests.get(f"http://localhost:5000/books/{id}")
    print(request)
    print(request.json())

def change_book(id):
    book = {"author": "Max Fisher", "id": 1, "title": "A máquina do caos"}
    request = requests.put(f"http://localhost:5000/books/{id}", json=book)
    print(request)
    print(request.json())

def create_book():
    book = {"id": 4, "autor": "Yuval Noah", "title": "Sapiens"}
    criate = requests.post("http://localhost:5000/books", json=book)
    print(criate)

def delete_book(id):
    delete = requests.delete(f"http://localhost:5000/books/{id}")
    print(delete)

get_all_books()
