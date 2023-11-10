import sys
import Adafruit_DHT
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity))

import socket
#Import time module
import time
#Import Adafruit module
import Adafruit_DHT
# Create a socket object
s = socket.socket()
# Define the port on which you want to connect
port = 12345
# connect to the server on local computer
s.connect(('address', port)) #use your laptop IP
while True:
# read from sensor
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#prepare data
data = str(temperature) + " " + str(humidity)
print (data)
# send data to the server
s.send(data.encode())
# pause for 1 seconds
time.sleep(1)
#close the channel
s.close()