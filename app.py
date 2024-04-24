from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_books():
    req_data = request.get_json()
    text = req_data['text']
    sourcetype = req_data['sourcetype']

    url = "https://api.ai21.com/studio/v1/summarize"

    payload = {
    "sourceType": sourcetype,
    "source": text
    }

    headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer esXWvK7bkyIeOLhZIZ2ILz8czje5LwXC"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        summary = response.json()['summary']
        print(summary)
    else:
        print("Error:", response.text)
    
    return summary

