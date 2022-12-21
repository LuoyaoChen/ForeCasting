
from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def insert():
    return render_template('insert.html')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('delete.html')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('update.html')




