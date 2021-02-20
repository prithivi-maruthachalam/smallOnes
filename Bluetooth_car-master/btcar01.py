import bluetooth
import RPi.GPIO as GPIO
import time
import os

#Kindly change the pin numbers according to your needs. Extra pins have been setup and used for indicator leds

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

for i in range(2):
    GPIO.output(21,True)
    GPIO.output(24,True)
    time.sleep(0.5)
    GPIO.output(21,False)
    GPIO.output(24,False)
    time.sleep(0.5)



def stoppen():
    GPIO.output(18,False)
    GPIO.output(14,False)
    GPIO.output(22,False)
    GPIO.output(23,False)

GPIO.output(21,True)

host = ""
port = 1

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("socket created")
GPIO.output(24,True)
time.sleep(0.55)
GPIO.output(24,False)
try:
    server.bind((host,port))
    print("binding completed")
    GPIO.output(24,True)
    time.sleep(0.55)
    GPIO.output(24,False)
except:
    print("binding failed")

server.listen(1)#number of connections at a time
client, address = server.accept()
print("connected to", address)
print("client", client)

GPIO.output(24,True)
time.sleep(1.5)
GPIO.output(24,False)
time.sleep(0.5)
GPIO.output(24,True)


try:
    while True:
        
        
        data = client.recv(1024)
        print(data)
        if data == b'lefta':
            GPIO.output(22,True)
            GPIO.output(18,True)

        elif data == b'leftb':
            stoppen()         

        elif data == b'fronta':
            GPIO.output(22,True)
            GPIO.output(23,True)
            
        elif data == b'frontb':
            stoppen()
            
        elif data == b'reva':
            GPIO.output(14,True)
            GPIO.output(18,True)
        

        elif data == b'revb':
            stoppen()
        

        elif data == b'righta':
            GPIO.output(23,True)
            GPIO.output(14,True)

        elif data == b'rightb':
            stoppen()

        elif data == "voice_stop":
            stoppen()

        elif data == b'softclose':
            GPIO.cleanup()
            client.close()
            server.close()
        
        elif data == b'close':
            GPIO.cleanup()
            os.system("sudo shutdown -h now")
            client.close()
            server.close()

        else:
            print("booyeah")


except:
    GPIO.cleanup()
    client.close()
    server.close()
    print("done")
		
		


            


