import requests
import random
import time
from datetime import datetime

API_URL = "http://10.17.131.42:5001/submit"  # Replace with your actual VM IP

def generate_fake_data(sensor_id):
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(15.0, 30.0), 2),  # °C
        "moisture": round(random.uniform(20.0, 80.0), 2),     # %
        "ph": round(random.uniform(5.5, 7.5), 2)              # pH
    }

def send_data():
    sensor_id = "sensor01"
    while True:
        payload = generate_fake_data(sensor_id)
        print(f"[{datetime.now()}] Sending: {payload}")
        try:
            response = requests.post(API_URL, json=payload)
            print(f"→ Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(30)  # wait 30 seconds before sending next reading

if __name__ == "__main__":
    send_data()