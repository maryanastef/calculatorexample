"""A simple flask web app"""
from flask import Flask, flash, render_template
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/table")
def table():
    """returns table"""
    return render_template("table.html")


@app.route("/article1")
def article1():
    """returns table"""
    return render_template("article1.html")


@app.route("/article2")
def article2():
    """returns table"""
    return render_template("article2.html")


@app.route("/article3")
def article3():
    """returns table"""
    return render_template("article3.html")


@app.route("/article4")
def article4():
    """returns table"""
    return render_template("article4.html")
