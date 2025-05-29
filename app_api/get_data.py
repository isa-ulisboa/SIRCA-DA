import requests
from datetime import datetime, timedelta

API_URL = "http://10.17.131.42:5001/data"  # Replace with your actual IP

def fetch_data(start, end, parameter):
    params = {
        "start": start,
        "end": end,
        "parameter": parameter
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        print(f"Retrieved {len(data)} records for '{parameter}'")
        for record in data:
            print(record)
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    # Example: last 24 hours
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)

    fetch_data(
        start=start_time.strftime("%Y-%m-%dT%H:%M"),
        end=end_time.strftime("%Y-%m-%dT%H:%M"),
        parameter="moisture"  # change to temperature or ph
    )