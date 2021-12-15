"""A simple flask web app"""
import pandas as pd
from flask import Flask, flash, render_template, request
from werkzeug.debug import DebuggedApplication
from controllers.calculator_controller import CalculatorController
from controllers.index_controller import IndexController
from calc.calculator import Calculator
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class CalculatorTable(db.Model):
    value1 = db.Column(db.Integer, primary_key=True)
    value2 = db.Column(db.Integer, index=True)
    operation = db.Column(db.String(256))
    result = db.Column(db.Integer, index=True)


db.create_all()


@app.route('/')
def index():
    item = CalculatorTable.query
    return render_template('table.html', title='Basic Table',
                           users=item)


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
    """returns article1"""
    return render_template("article1.html")


@app.route("/article2")
def article2():
    """returns article2"""
    return render_template("article2.html")


@app.route("/article3")
def article3():
    """returns article3"""
    return render_template("article3.html")


@app.route("/article4")
def article4():
    """returns article4"""
    return render_template("article4.html")


if __name__ == '__main__':
    app.run()