import requests
URL = os.getenv('API_URL') # Get the API URL from environment variables.
import os


def extract_data():
    response = requests.get(URL) # Make a GET request to the API URL.

    return response.json()['PublicAssistanceFundedProjectsDetails'] # Return the JSON response.