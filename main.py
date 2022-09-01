# first install requests: sudo pip3 install requests
from flask import Flask
import requests
import sys
import json

app = Flask(__name__)

@app.route('/temperature/<city>')
def temperature(city):
    payload = {'APPID': 'YOUR_API_KEY_HERE', 'q':city}
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(URL, params = payload)
    if response.status_code == 200:
        print('Success!', file = sys.stdout)
    elif response.status_code == 404:
        print('Not found.', file=sys.stdout)

    response_json = response.json()
    formatted_response = json.dumps(response_json, indent = 2)
    print(formatted_response, file=sys.stdout)

    temperature = response_json['main']['temp']
    s = '<h> Current temperature in {} is {:0.2f} Celsius. </s>'
    return s.format(city, temperature - 273)
