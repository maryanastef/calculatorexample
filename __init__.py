from flask import Flask, render_template, flash
from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("base.html")


@app.route('/index/')
def dashboard():
    flash("flash test!!!!")
    flash("fladfasdfsaassh test!!!!")
    flash("asdfas asfsafs!!!!")
    return render_template("index.html", TOPIC_DICT=TOPIC_DICT)
