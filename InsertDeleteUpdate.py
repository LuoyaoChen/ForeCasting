import mysql.connector
from mysql.connector import errorcode

def operate_one_row(one_table_name, op = None, 
                    table_columns=tuple(), new_content = tuple()):
  assert op in ['insert', 'update', 'delete']
  # Obtain connection string information from the portal
  config = {
      'host': 'diabetesforecast.mysql.database.azure.com',
      'user': 'cly',
      'password': 'DMSFALL2022%-',
      'database': 'chronic',
      'client_flags': [mysql.connector.ClientFlag.SSL],
      'ssl_ca': './DigiCertGlobalRootCA.crt.pem'
  }

  # Construct connection string

  try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  else:
    cursor = conn.cursor()
    
    cursor.execute(f"select * from {one_table_name};")
    res = cursor.fetchall()
    if cursor.rowcount==0 and op=="delete": ## counter for when row count ==0 
      return []
    
    ################### insert a data row in the table ###################
    if op == "insert":
      query = f"INSERT INTO {one_table_name}("+ ",".join(table_columns) + f") VALUES {str(new_content)};"
      # print(f"query = {query}")
      cursor.execute(query) ## do insert 
      cursor.execute(f"select * from {one_table_name}") ## need to return the result
      table_content = cursor.fetchall()
      print(f"table_content = {table_content}")
      
    ################### Update a data row in the table ###################
    elif op == 'update':
      idx_tobe_updated = new_content[0]
      print(f"idx_tobe_updated = {idx_tobe_updated}")
      query1 = f"update {one_table_name} set {table_columns[1]} = '{new_content[1]}' where Id = {idx_tobe_updated};"
      query2 = f"update {one_table_name} set {table_columns[2]} = '{new_content[2]}' where Id = {idx_tobe_updated};"
      query3 = f"update {one_table_name} set {table_columns[3]} = '{new_content[3]}' where Id = {idx_tobe_updated};"
      # print(f"query1 = {query1}\nquery2 = {query2}\nquery3 = {query3}")

      cursor.execute(query1) ## update
      cursor.execute(query2) ## update
      cursor.execute(query3) ## update

      cursor.execute(f"select * from {one_table_name}") ## need to return the result
      table_content = cursor.fetchall()
      print(f"table_content = {table_content}")
    
    ################### Delete a data row in the table ###################
    elif op =='delete': 
      query = f"select Id from {one_table_name} order by Id desc limit 1"
      cursor.execute(query) ## delete
      max_id = cursor.fetchall()[0][0]       
      cursor.execute(f"DELETE FROM {one_table_name} where id = {max_id};")
      cursor.execute(f"select * from {one_table_name}")
      table_content = cursor.fetchall()
    


    
    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    return table_content
    
    
    
  

if __name__ == "__main__":
  ## test delete
  # table_content = operate_one_row(one_table_name = "inventory", op = 'delete')
  
  # ## test insert
  # table_content = operate_one_row(one_table_name = "inventory", 
  #                                 op = 'insert',  
  #                                 table_columns=['Id', 'name', 'quantity', 'place'], 
  #                                 new_content = str((17, 'pear', 1, 'us')))
  
  ## test update
  table_content = operate_one_row(one_table_name = "inventory", op = 'update',
                                  table_columns=['Id', 'name', 'quantity', 'place'],
                                  new_content = ('10', 'yes', '211', 'austrialia'))

  print(f"table_content = {table_content}")
