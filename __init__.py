from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("base.html")
