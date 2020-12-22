import webview
from flask import Flask, render_template, request

server = Flask(__name__, static_folder='./assets', template_folder='./templates')


@server.route("/", methods = ['GET', 'POST'])
def home():
    return render_template("home.html")


window = webview.create_window(
    title="Library Management",
    width=1366,
    height=768,
    url=server,
)
webview.start()
