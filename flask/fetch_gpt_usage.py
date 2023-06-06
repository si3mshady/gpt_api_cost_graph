from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from flask_cors import CORS
import requests
import time




API_KEY = ""
# API_ENDPOINT = "https://api.openai.com/dashboard/billing/usage?end_date=2023-07-01&start_date=2023-06-01"
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requestsx

usage_data = []



def generate_api_endpoint_days_back(days_back=7):
    # Get the current date
    end_date = datetime.now().strftime('%Y-%m-%d')
    # Calculate the start date based on the specified number of days back
    start_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    # Generate the date string
    date_string = f"end_date={end_date}&start_date={start_date}"
    API_ENDPOINT = f"https://api.openai.com/dashboard/billing/usage?{date_string}"
    return API_ENDPOINT


def track_api_usage():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        print('Starting data collection...')
        
        response = requests.get(generate_api_endpoint_days_back(), headers=headers)
        if response.status_code == 200:
            data = response.json()
    

            usage = data['total_usage']
            print(usage)
            usage_data.append({
               'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'cost': usage
            })
            print(usage_data)
            print('New data collected')

        time.sleep(3)  # Track usage every 3 seconds
    except Exception as e:
        print(str(e))

@app.route("/api/usage", methods=["GET"])
def get_api_usage():
    track_api_usage()
    
    return jsonify(usage_data)


    # return jsonify([(usage_data)[-1]])

if __name__ == "__main__":
    # Start a background thread to track API usage
    # import threading
    # t = threading.Thread(target=track_api_usage)
    # t.start()

    app.run(debug=True, port=5000, host='0.0.0.0')
    
