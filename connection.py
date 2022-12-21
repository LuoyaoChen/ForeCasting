import mysql.connector
from mysql.connector import errorcode

def connect_to_cursor(one_table_name=None, task='get_table_contents'):
  # Obtain connection string information from the portal
  config = {
      'host': 'diabetesforecast.mysql.database.azure.com',
      'user': 'cly',
      'password': 'DMSFALL2022%-',
      'database': 'chronic',
      'client_flags': [mysql.connector.ClientFlag.SSL],
      # 'client_flags': [2048],
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

    ################## Drop previous table of same name if one exists ###################
    cursor.execute("DROP TABLE IF EXISTS inventory;")
    print("Finished dropping table (if existed).")

    ################### Create table ###################
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER, place VARCHAR(50));")
    print("Finished creating table.")

    # Insert some data into table
    cursor.execute("INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("banana", 150, "US"))
    print("Inserted",cursor.rowcount,"row(s) of data.")
    cursor.execute("INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("orange", 154, "US"))
    print("Inserted",cursor.rowcount,"row(s) of data.")
    cursor.execute("INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("apple", 100,"US"))
    print("Inserted",cursor.rowcount,"row(s) of data.")
    cursor.execute(
        "INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("yes", 100, "US"))
    print("Inserted", cursor.rowcount, "row(s) of data.")
    # print(f"task = {task}")
    if task == 'get_table_names':
        #### get table names  #### ref = https://stackoverflow.com/questions/3556305/how-to-retrieve-table-names-in-a-mysql-database-with-python-and-mysqldb
        cursor.execute("USE chronic")
        cursor.execute("SHOW TABLES")
        all_table_names = cursor.fetchall() 
        table_names = [t[0] for t in all_table_names]
        print(f"tables = {table_names}") ## tables = ['accounnmember', 'account', 'account_admin', 'account_alias', 'associate', 'biling_account', 'contract', 'contractbenefit', 'contractplayingrole', 'contractpremium', 'customer', 'customer_address', 'inventory', 'manager_contract', 'product', 'scores']
        return table_names
    elif task == 'get_table_contents':
        # print("in task == get_table_contents")
        cursor.execute("SELECT * FROM " + one_table_name + ";")
        table_content = cursor.fetchall()
        return table_content
    
    #### Cleanup ####
    conn.commit()
    cursor.close()
    conn.close()

if __name__ =="__main__":
  table_names = connect_to_cursor(one_table_name='inventory', task='get_table_names')
  for name in table_names:
    print(name)
  table_content = connect_to_cursor(one_table_name='inventory', task='get_table_contents')
  for row in table_content:
    print(row)