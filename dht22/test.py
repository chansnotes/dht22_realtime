import time
import board
import adafruit_dht
import datetime
import csv

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D26)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

header = ['Timestamp', 'Temperature(C)', 'Humidity(%)']

current_date = datetime.datetime.now().strftime("%Y_%m_%d")
f = open("tempeh_{}.csv".format(current_date), 'a+')
writer = csv.writer(f)
writer.writerow(header)
f.close()

while True:
   # current_date = datetime.datetime.now().strftime("%Y_%m_%d")
   # f = open("tempeh_{}".format(current_date), 'a+')
   # writer = csv.writer(f)
    try:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
       # temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Timestamp: {} , Temp: {:.1f} C ,   Humidity: {}% ".format(
                current_time, temperature_c, humidity
            )
        )
        with open("tempeh_{}.csv".format(current_date),'a+') as file:
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
        time.sleep(5.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        #f.close()
        raise error

    time.sleep(5.0)
