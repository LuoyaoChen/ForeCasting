import mysql.connector
from mysql.connector import errorcode

def operate_one_row(one_table_name, op = None, table_columns=tuple(), new_content = tuple()):
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
    if cursor.rowcount==0: ## counter for when row count ==0 
      return []
    
    ################### insert a data row in the table ###################
    if op == "insert":
      cursor.execute(
          f"INSERT INTO {one_table_name} {table_columns} VALUES new_content;")
      table_content = cursor.fetchall()
      
    ################### Delete a data row in the table ###################
    elif op =='delete': 
      cursor.execute(f"select id from {one_table_name} order by id desc limit 1")
      max_id = cursor.fetchall()[0][0]       
      cursor.execute(f"DELETE FROM {one_table_name} where id = {max_id};")
      cursor.execute(f"select * from {one_table_name}")
      table_content = cursor.fetchall()
    
    ################### Update a data row in the table ###################
    # elif op == 'update':
    
    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    return table_content
    
    
    
  

if __name__ == "__main__":
  # table_content = operate_one_row(one_table_name = "inventory", op = 'delete')
  table_content = operate_one_row(one_table_name = "inventory", 
                                  op = 'insert',  
                                  table_columns=('id', 'name', 'quantity', 'place'), 
                                  new_content = (1, 'pear', 1, 'us'))

  print(f"table_content = {table_content}")
