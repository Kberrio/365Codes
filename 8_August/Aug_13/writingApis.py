# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger
import os

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production!

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Init JWT
jwt = JWTManager(app)

# Init Swagger
swagger = Swagger(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    author = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __init__(self, title, author, description, price):
        self.title = title
        self.author = author
        self.description = description
        self.price = price

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

# Book Schema
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'price')

# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Create a book
@app.route('/book', methods=['POST'])
@jwt_required()
def add_book():
    """
    Create a new book
    ---
    tags:
      - books
    parameters:
      - in: body
        name: body
        schema:
          id: Book
          required:
            - title
            - author
            - description
            - price
          properties:
            title:
              type: string
            author:
              type: string
            description:
              type: string
            price:
              type: number
    responses:
      201:
        description: Created
      400:
        description: Invalid input
    """
    title = request.json['title']
    author = request.json['author']
    description = request.json['description']
    price = request.json['price']

    new_book = Book(title, author, description, price)

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book), 201

# Get all books
@app.route('/book', methods=['GET'])
def get_books():
    """
    Get all books
    ---
    tags:
      - books
    responses:
      200:
        description: A list of books
    """
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)

# Get single book
@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    """
    Get a book by ID
    ---
    tags:
      - books
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: A single book
      404:
        description: Book not found
    """
    book = Book.query.get(id)
    if book:
        return book_schema.jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Update a book
@app.route('/book/<id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    """
    Update a book
    ---
    tags:
      - books
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          id: BookUpdate
          properties:
            title:
              type: string
            author:
              type: string
            description:
              type: string
            price:
              type: number
    responses:
      200:
        description: Book updated
      404:
        description: Book not found
    """
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    title = request.json.get('title', book.title)
    author = request.json.get('author', book.author)
    description = request.json.get('description', book.description)
    price = request.json.get('price', book.price)

    book.title = title
    book.author = author
    book.description = description
    book.price = price

    db.session.commit()

    return book_schema.jsonify(book)

# Delete a book
@app.route('/book/<id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    """
    Delete a book
    ---
    tags:
      - books
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Book deleted
      404:
        description: Book not found
    """
    book = Book.query.get(id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted"})

# User registration
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - users
    parameters:
      - in: body
        name: body
        schema:
          id: UserRegistration
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      201:
        description: User created
      400:
        description: Username already exists
    """
    username = request.json['username']
    password = request.json['password']

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    """
    User login
    ---
    tags:
      - users
    parameters:
      - in: body
        name: body
        schema:
          id: UserLogin
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful
      401:
        description: Invalid username or password
    """
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Invalid username or password"}), 401

# Run server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)