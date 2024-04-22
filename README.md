# api_books

### Descrição

A api_books foi criada para o armazenamento de livros de sua preferencia, sendo assim, você tem total controle para criar, editar, alterar e/ou excluir livros. 
- As alterações não são permanentes

### Objetivo

O objetivo dessa api é disponibilizar a consulta, criação, edição e exclusão de livros.

### Recursos

No momento a api_books está disponibilizando 3 livros para consulta.

### Retornar todos os livros (GET)

- http://localhost:5000/books

Exemplo de consulta 
```python
request = requests.get('http://localhost:5000/books')
print(request.json())
```
Retorno
- Retorna uma lista de todos os livros da api em formato json

```python
[{'author': 'Max Fisher', 'id': 1, 'title': 'A máquina do caos'}, {'author': 'Bill Gates', 'id': 2, 'title': 'A estrada do futuro'}, {'author': 'Jeanine Cummins', 'id': 3, 'title': 'Terra Americana'}]
```

### Retornar um livro (GET)
- Para cada id(livro) que você acessa com o método GET, é retornado o id, nome do autor e o título do livro.
- Use id de 1 a 3
- http://localhost:5000/books/{id}

exemplo de consulta por id
```python
request = requests.get(f"http://localhost:5000/books/{id}")
print(request.json())
```

### Fazer alterações (PUT)
- Não esqueça de específicar o livro que você deseja alterar. Para fazer isso basca acrescentar o número do id do livro na rota.
- http://localhost:5000/books/{id}

Exemplo de alteração por id
```python
book = {"author": "Max Fisher", "id": 1, "title": "A Máquina do Caos"}
request = requests.put(f"http://localhost:5000/books/{id}", json=book)
print(request.json())
```

Retorno
```python
{'author': 'Max Fisher', 'id': 1, 'title': 'A Máquina do Caos'}
```

### Para criar um livro (POST)
- http://localhost:5000/books

Exemplo de criação de um livro
```python
book = {"id": 4, "autor": "Yuval Noah", "title": "Sapiens"}
criate = requests.post("http://localhost:5000/books", json=book)
print(criate)
```

Retorno
- O código HTTP 200 quer dizer que a requisição foi feita com sucesso.

```python
<Response 200>
```
 
### Para deletar um livro (DELETE)
- http://localhost:5000/books/{id}

Exempo de exclusão de um livro
```python
delete = requests.delete(f"http://localhost:5000/books/{id}")
print(delete)
```

Retorno
```python
<Response 200>
```



Para executar essa API é preciso clonar esse repositório.
