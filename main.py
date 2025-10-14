# Create a virtual environment.
# Activate the virtual environment.
# Import request which is used to make HTTP requests.pip
# View a ist of installed packages.
# Start project
# docker-compose up is the command that starts all the services defined in your docker-compose.yml.
# The project starts with API connection and settingup the postgres database
# configure postgres database

from dotenv import load_dotenv #dotenv is used to hide sensitive information like API keys.
from .elt.db_connect import conn, cur, insert_query #Import the database connection and cursor from db_connect.py.
from .elt.extract import extract_data # Import the extract_data function from extract.py.

load_dotenv() # Load environment variables from a .env file.







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
    


