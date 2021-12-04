import time
import board
import adafruit_dht
import datetime
import csv
from flask import Flask, render_template

app = Flask(__name__)

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D26)

@app.route('/')
def main():
    curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    templateDate = {
        'temperature': temperature_c,
        'humidity' : humidity,
        'time' : curr_time
    }

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
