import requests, json
import serial

while True:
    signals = json.loads(requests.get('http://127.0.0.1:5000/').text)
    if signals['right']:
        
    elif signals['left']:
