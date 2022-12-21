from flask import Flask, redirect, url_for, render_template, request, abort
import mysql.connector
from mysql.connector import errorcode

from connection import connect_to_cursor
app = Flask(__name__)

@app.route('/')
def homepage():
    table_names = connect_to_cursor(task='get_table_names')
    return render_template("homepage.html", 
                           table_names=table_names
                           )


@app.route('/tables/<table_name>/')
def one_table(table_name):
    table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
    return render_template("one_table.html",
                           table_name = table_name,
                        table_content = table_content)







# '''
# take in input from usr 
# '''
# @app.route('/')
# def student():
#    return render_template('student.html')

# '''
# put into result table
# '''
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# @app.route('/', methods=['GET', 'POST'])
# def insert():
#     return render_template('insert.html')




