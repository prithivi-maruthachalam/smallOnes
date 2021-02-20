import RPi.GPIO as GPIO
import dht11
import time
import datetime
from matplotlib import pyplot as plt
import csv
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
dest = "xyz@gmail.com"
server.starttls()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

server.login("abc@gmail.com", "pass")

instance = dht11.DHT11(pin=18)
tim = []
hum = []
temp = []
data = []
plt.ion()
a = 0
count = 0
zeg = 0
           
try:
    while True:
        result = instance.read()
        if result.is_valid():
        
            tim.append(datetime.datetime.now())
            temp.append(result.temperature)
            hum.append(result.humidity)
            data.append([result.humidity,datetime.datetime.now()])
            zeg = zeg + 1
            if int(result.humidity) > 93 and zeg%2 == 0:
                print('hey!!')
                msg = "WARNING! Unnatural humidity reading detected!" # The /n separates the message from the headers
                server.sendmail("", dest, msg)
                GPIO.output(27,True)
                time.sleep(1)
                GPIO.output(27,False)
                
                
            count = count + 1
            if (count % 5) == 0:
                with open('/home/pi/DHT11_Python/pop.csv', 'a') as csvfile:
                    cs = csv.writer(csvfile,delimiter = ',')
                    for line in data:
                        cs.writerow(line)

            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            print(hum)

            a = a + 1

            if (a % 10) == 0:
                plt.plot(tim,hum)
                plt.show()
                plt.pause(0.0001)
        time.sleep(1)

finally:
    GPIO.output(27,False)
    GPIO.cleanup()
    

