import mysql.connector
from mysql.connector import errorcode

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

  ################### Drop previous table of same name if one exists ###################
  cursor.execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")

  ################### Create table ###################
  cursor.execute(
      "CREATE TABLE inventory (Id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER, place VARCHAR(50));")
  print("Finished creating table.")

  # Insert some data into table
  cursor.execute(
      "INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("banana", 150, "AUS"))
  print("Inserted", cursor.rowcount, "row(s) of data.")
  cursor.execute(
      "INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("orange", 154, "AUS"))
  print("Inserted", cursor.rowcount, "row(s) of data.")
  cursor.execute(
      "INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("apple", 100, "AUS"))
  cursor.execute(
      "INSERT INTO inventory (name, quantity, place) VALUES (%s, %s, %s);", ("straberry", 20, "AUS"))
  print("Inserted", cursor.rowcount, "row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()