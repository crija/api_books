# api_books

Descrição:
A api_books foi criada para o armazenamento de livros de sua preferencia, sendo assim, você tem total controle para criar, editar, alterar e/ou excluir livros. 

Objetivo:

O objetivo dessa api é disponibilizar a consulta, criação, edição e exclusão de livros.

Recursos:

No momento a api_books está disponibilizando 3 livros para consulta. Para cada id(livro) que você acessa com o método GET, é retornado o id, nome do autor e o título do livro.

Exemplo de consulta por id
```python
def change_book(id):
    book = {"author": "Max Fisher", "id": 1, "title": "A máquina do caos"}
    request = requests.put(f"http://localhost:5000/books/{id}", json=book)
    print(request)
    print(request.json())
```

respota



Acessar api:

 Para retornar todos os livros use o método (GET)
- http://localhost:5000/books

Para retornar um livro, use o método (GET)
Use id de 1 a 3
- http://localhost:5000/books/{id}

Para fazer alteração pelo id, use o método (PUT)
- http://localhost:5000/books/{id}

Para criar um livro, use o método (POST)
- http://localhost:5000/books

Para deletar o livro pelo id, use o método (DELETE)
- http://localhost:5000/books/{id}

Para executar essa API é preciso clonar esse repositório.
