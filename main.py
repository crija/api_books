from flask import Flask
from routes.home import home_route
from routes.books import books_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(books_route, url_prefix='/books')

# Execuxao
app.run(debug=True)