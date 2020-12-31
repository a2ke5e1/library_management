import webview
from flask import Flask, render_template, request, redirect, url_for
from console_app import app_console
from db import Books


def app(debug=False):
    server = Flask(__name__, static_folder='./assets', template_folder='./templates')
    window = webview.create_window(
        title="Library Management",
        width=1366,
        height=768,
        min_size=(500, 400),
        background_color="#292929",
        url=server,
    )

    @server.route("/books/view/")
    def booksView():
        return redirect('/books/view/1-10')

    @server.route("/books/view/<int:back>-<int:next>")
    def booksViewWithRange(back, next):

        if next < back :
            return redirect('/books/view/1-10')

        if len(Books().get_range(back, next)) == 0:
            return redirect(f'/books/view/{back - 10}-{next - 10}')

        return render_template("/books/books.html", books=Books().get_range(back, next), back=back, next=next)

    @server.route("/books/add", methods = ['POST', 'GET'])
    def addBook():
        if request.method == 'POST':
            book_name = request.form.get('book_name')
            book_author =request.form.get('book_author')
            book_isbn =request.form.get('book_isbn')
            Books().add(book_name,book_author,book_isbn)
            return redirect(f'/books/view/', )
        else :
            return render_template("/books/book_add.html")

    @server.route("/books/delete/<int:book_id>",  methods=['POST'])
    def deleteBookId(book_id):
        Books().delete(book_id,)
        return redirect("/books/view")

    @server.route("/books/update/<int:book_id>", methods=['POST', 'GET'])
    def updateBook(book_id):
        if request.method == 'POST':
            book_name = request.form.get('book_name')
            book_author = request.form.get('book_author')
            book_isbn = request.form.get('book_isbn')
            Books().update_byId(book_id,book_name,book_author,book_isbn)
            return redirect(f'/books/view/')
        else:
            book = Books().get_byId(book_id)
            return render_template("/books/book_update.html", book=book)

    @server.route("/", methods=['GET', 'POST'])
    def home():
        return render_template("/home.html")

    @server.route("/console")
    def console():
        app_console()
        return "Close This Window"

    if debug:
        server.run()
    else:
        webview.start()


if __name__ == "__main__":
    app(debug=True)
