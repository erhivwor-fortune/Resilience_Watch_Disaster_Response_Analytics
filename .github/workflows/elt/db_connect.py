import psycopg2 # PostgreSQL database adapter for Python.

conn = psycopg2.connect(
    host = 'localhost',
    port = 5434, # postgres on your laptop is 5432. user is postgress, paswd:1234. docker is 5434(outside network, 5432 is for the same network).
    database = 'disaster_insurance',
    user = 'admin', #if using docker, its admin for both user and password. 
    password = 'admin'
) # Connect to the PostgreSQL database.
cur = conn.cursor() # Create a cursor object to interact with the database.

#We dockerized this code so that we can run on different platform: linus, mac, windows.
#This code helps us connect to the API.
cur.execute("""
    CREATE TABLE IF NOT EXISTS disaster (
        disasterNumber INT, 
        incidentType TEXT,
        projectSize TEXT
    )
""") # Create a table to store insurance data if it doesn't exist.


#cor = conn.cursor()

# Code to insert data into the table. # %s are placeholders that helps you avoid sql injection.
insert_query = """ 
    INSERT INTO disaster (disasterNumber, incidentType, projectSize)
    VALUES (%s, %s, %s)
 
 """