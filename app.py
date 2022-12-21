from flask import Flask, redirect, url_for, render_template, request, abort
from mysql.connector import errorcode

from connection import connect_to_cursor
import connect_ml
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
    
@app.route('/estimate_price', methods=['POST', 'GET'])
def estimate_price():
   if request.method == 'POST':
      input_info = request.form
      processed_data = connect_ml.web_input(input_info)
      estimate_price = connect_ml.make_prediction(processed_data)
      return render_template("estimate_price.html", estimate_price=estimate_price[0])
    




if __name__ == '__main__':
   app.run(debug=True)








