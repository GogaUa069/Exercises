from flask import Flask

myapp = Flask(__name__)


@myapp.route("/")
def hi():
    return "Hello! I'm Goga!"


myapp.run()
