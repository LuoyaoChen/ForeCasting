import mysql.connector
from mysql.connector import errorcode

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

  ################### Delete a data row in the table ###################
  cursor.execute("DELETE FROM inventory WHERE name=%(param1)s;", {'param1':"orange"})
  print("Deleted",cursor.rowcount,"row(s) of data.")
  

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()