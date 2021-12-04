import time
import board
import adafruit_dht
from datetime import datetime
import sqlite3
import csv

DB_NAME="./db/dht.db"
dhtDevice = adafruit_dht.DHT22(board.D26)

conn = sqlite3.connect(DB_NAME, isolation_level=None)
cur = conn.cursor()

header = ['Timestamp', 'Temperature(C)', 'Humidity(%)']

current_date = datetime.now().strftime("%Y_%m_%d")
f = open("./csv/tempeh_{}.csv".format(current_date), 'a+')
writer = csv.writer(f)
writer.writerow(header)
f.close()


while True:
   # current_date = datetime.datetime.now().strftime("%Y_%m_%d")
   # f = open("tempeh_{}".format(current_date), 'a+')
   # writer = csv.writer(f)
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
       # temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Timestamp: {} , Temp: {:.1f} C ,   Humidity: {}% ".format(
                current_time, temperature_c, humidity
            )
        )
        now = datetime.now()
        current = now.strftime("%H:%M:%S")
        cur.execute('insert into tbth values(?, ?, ?)', (temperature_c, humidity, now.isoformat()))


        with open("./csv/tempeh_{}.csv".format(current_date),'a+') as file:
                writer = csv.writer(file)
                data = [current_time, temperature_c, humidity]
                writer.writerow(data)

       # f = open("tempeh_{}.csv".format(current_date), 'a+')
       # writer = csv.writer(f)
       # data = [current_time, temperature_c, humidity]
       # writer.writerow(data)
       # f.close()

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        f.close()
        raise error

    time.sleep(5.0)

conn.close()
