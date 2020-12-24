import webview
from flask import Flask, render_template, request


def app(debug=False):
    server = Flask(__name__, static_folder='./assets', template_folder='./templates')

    @server.route("/", methods=['GET', 'POST'])
    def home():
        return render_template("home.html")

    if debug:
        server.run()
    else:
        window = webview.create_window(
            title="Library Management",
            width=1366,
            height=768,
            min_size=(500, 400),
            url=server,
        )
        webview.start()


app(debug=False)
