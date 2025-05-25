import datetime
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("HOSTED_API")

def fetch_api_data():
    if not API_URL:
        print(f"[{datetime.datetime.now()}] Error: HOSTED_API is not set.")
        exit(1)

    for i in range(10):
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                data = response.json()
                print(f"[{datetime.datetime.now()}] API Response {i+1}:", data)
            else:
                print(f"[{datetime.datetime.now()}] Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"[{datetime.datetime.now()}] Exception occurred: {e}")
        if i < 7:  
            time.sleep(15)

    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            print(f"[{datetime.datetime.now()}] API Response:", data)
        else:
            print(f"[{datetime.datetime.now()}] Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Exception occurred: {e}")

if __name__ == "__main__":
    fetch_api_data()