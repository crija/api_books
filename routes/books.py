from flask import Blueprint, render_template

books_route = Blueprint('books', __name__)

# Lista os Livros
@books_route.route('/')
def book_list():
   return{'página': "Lista_Livros"}

# Cadastra Livro
@books_route.route('/', methods=['POST'] )
def add_book():
   pass

# Renderiza Formulário
@books_route.route('/new')
def register_form():
   return{'formulário': "Formulario_cadastro"}

# Busca Livro
@books_route.route('/')
def get_book(book_id):
   pass
    
# Livros Id
@books_route.route('/<int:book_id>')
def book_id(book_id):
   pass 

# Formulário para editar cadastro
@books_route.route('/<int:book_id>/edit')
def form_edit(book_id):
   pass 

# Atualiza livro
@books_route.route('/<int:book_id>/update', methods=['PUT'])
def update_book(book_id):
   pass 

# Deleta Livro
@books_route.route('/<int:book_id>/delete', methods=['DELETE'])
def delete_book(book_id):
   pass 