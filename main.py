import webview
from flask import Flask, render_template, request
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

    @server.route("/books/view")
    def booksView():
        return render_template("/books/books.html", books=Books().get_all())

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
    app(debug=False)
