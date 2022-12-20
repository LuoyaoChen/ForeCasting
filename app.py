
from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__)
mysql = MySQL(app)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


