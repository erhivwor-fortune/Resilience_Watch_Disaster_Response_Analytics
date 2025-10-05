# Create a virtual environment.
# Activate the virtual environment.
# Import request which is used to make HTTP requests.pip
# View a ist of installed packages.
# Start project
# docker-compose up is the command that starts all the services defined in your docker-compose.yml.
# The project starts with API connection and settingup the postgres database
# configure postgres database
import requests
from dotenv import load_dotenv #dotenv is used to hide sensitive information like API keys.
import os
import psycopg2 # PostgreSQL database adapter for Python.

load_dotenv() # Load environment variables from a .env file.

URL = os.getenv('API_URL') # Get the API URL from environment variables.

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

def extract_data():
    response = requests.get(URL) # Make a GET request to the API URL.

    return response.json()['PublicAssistanceFundedProjectsDetails'] # Return the JSON response.

insurance_data = []

def main():
    data = extract_data() # Extract data from the API.
    
    insurance_data.extend(data) # Extend the insurance_data list with the extracted data.

# use forloop to send data into postgres using a list comprehension.
    postgres_data = [ (data['disasterNumber'], data['incidentType'], data['projectSize'])for data in insurance_data ]

# send data to postgres table
    cur.executemany(insert_query, postgres_data) # Insert data into the PostgreSQL database.

    conn.commit()
    cur.close()
    conn.close()

    print("Data inserted successfully")

    return None

if __name__ == "__main__":
    main() 
    


