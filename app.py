from flask import Flask, redirect, url_for, render_template, request, abort
from mysql.connector import errorcode

from connection import connect_to_cursor
from InsertDeleteUpdate import operate_one_row
import connect_ml
app = Flask(__name__)

@app.route('/')
def homepage():
    table_names = connect_to_cursor(task='get_table_names')
    return render_template("homepage.html", 
                           table_names=table_names
                           )

@app.route('/estimate_price', methods=['POST', 'GET'])
def estimate_price():
   if request.method == 'POST':
      input_info = request.form
      processed_data = connect_ml.web_input(input_info)
      estimate_price = connect_ml.make_prediction(processed_data)
      return render_template("estimate_price.html", estimate_price=estimate_price[0])
  
@app.route('/tables/<table_name>/')
def one_table(table_name):
    table_columns, table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
   #  table_content = operate_one_row(one_table_name=table_name, op = "delete")
    return render_template("one_table.html",
                           table_name = table_name,
                           table_columns = table_columns,
                        table_content = table_content)


@app.route('/tables/<table_name>/insert_one_row/', methods=['POST'])
def one_table_insert(table_name):
    table_columns, table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
    if request.method == 'POST':
      res = request.form
      to_be_inserted = []
      for _, user_input_value in res.items():
         to_be_inserted.append(user_input_value)
      table_content = operate_one_row(one_table_name=table_name, op = "insert", table_columns = table_columns, new_content = tuple(to_be_inserted))
      return render_template("one_table_insert.html",
                           table_name = table_name,
                           table_columns = table_columns,
                           table_content = table_content)
    
@app.route('/tables/<table_name>/update/', methods=['GET','POST'])
def update(table_name):
   table_columns, table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
   return render_template("update.html",
                           table_name=table_name,
                           table_columns=table_columns,
                           table_content=table_content)
   
@app.route('/tables/<table_name>/update/update_one_row/', methods=['GET', 'POST'])
def one_table_update(table_name):
   table_columns, table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
   res = request.form
   to_be_updated = []
   for _, user_input_value in res.items():
      to_be_updated.append(user_input_value)
   table_content = operate_one_row(one_table_name=table_name, op = "update", 
                                    table_columns = table_columns, 
                                    new_content = tuple(to_be_updated))
   return render_template("one_table_update.html",
                        table_name = table_name,
                           table_columns = table_columns,
                           table_content = table_content)

@app.route('/tables/<table_name>/delete_last_row/', methods=['POST', 'GET'])
def one_table_delete(table_name):
    table_columns, table_content = connect_to_cursor(one_table_name=table_name, task="get_table_contents")
    table_content = operate_one_row(one_table_name=table_name, op = "delete")
    if len(table_content) == 0:
       table_content = []
   #  result = request.form
   #  if result.method == 'POST':
   #     return redirect(url_for('one_table', table_name = table_name))
    return render_template("one_table_delete.html",
                           table_name = table_name,
                           table_columns = table_columns,
                           table_content = table_content)
    

    



if __name__ == '__main__':
   # app.run(debug=True)
   # one_table_delete(table_name = 'inventory')
   one_table_insert('inventory')
 







