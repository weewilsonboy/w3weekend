from flask import render_template, Blueprint, request, redirect
from models.book_list import book_list
from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route('/books')
def index():
    return render_template('index.jinja', title = "Book List", book_list=book_list)


@book_blueprint.route('/books', methods=['POST'])
def add_book():
    new_title = request.form['title']
    new_author = request.form['author']
    new_genre = request.form['genre']
    new_book = Book(new_title, new_author, new_genre)
    book_list.append(new_book)
    return render_template('index.jinja', title = "Book List", book_list=book_list)



@book_blueprint.route('/books/openindex/<name>', methods= ['POST'])
def open_index(name):
    return render_template('single.jinja', title = name, book = [i for  i in book_list if name == i.title])

@book_blueprint.route('/books/deleteindex', methods= ['POST'])
def remove_index():
    book_list.pop(int(request.form["index"]))
    return redirect('/books')
