import RPi.GPIO as GPIO
import time
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.cleanup()

m1f = 21
m1b = 22
m2b = 18
m2f = 23

GPIO.setup(m1f, GPIO.OUT)
GPIO.setup(m1b, GPIO.OUT)
GPIO.setup(m2f, GPIO.OUT)
GPIO.setup(m2b, GPIO.OUT)

pivot_time = 0.6



try:
    comm1 = serial.Serial('/dev/ttyUSB1',9600)
    handshake = str(comm1.readline().decode().strip())

except serial.serialutil.SerialException as e:
    comm1 = serial.Serial('/dev/ttyUSB0',9600)
    handshake = str(comm1.readline().decode().strip())

def stop():
    GPIO.output(m1f,False)
    GPIO.output(m2f,False)
    GPIO.output(m1b,False)
    GPIO.output(m2b,False)


def front():
    GPIO.output(m1f,True)
    GPIO.output(m2f,True)


def pivot_right():
    GPIO.output(m1b,True)
    GPIO.output(m2f,True)

def pivot_left():
    GPIO.output(m1f,True)
    GPIO.output(m2b,True)


def get_max_dir():
    comm1.write(b'give_d')
    max_d = int(comm1.readline())
    return max_d

if handshake == 'hi':
    comm1.write(b'pihi')
    if str(comm1.readline().decode().strip()) == ("pihi"):
        print("Handshake occurred!")
        print("starting logic loop")



try:
    while True:

        while True:
            max_direction = get_max_dir()
            if max_direction in (0, 1, 2):
                break
            else:
                continue
            
        print("getting max direction")
        if max_direction == 0:
            pivot_left()
            time.sleep(pivot_time)
            stop()

        elif max_direction == 2:
            pivot_right()
            time.sleep(pivot_time)
            stop()

        elif max_direction == 1:
            pass

        elif max_direction == 8:
            print("else block has been executed. condition did not get satisfied.")

        else:
            print(comm1.readline())
            

        comm1.write(b'need_distances')
        

        while(int(comm1.readline().decode().strip()) > 16):
            print(comm1.readline().decode().strip())
            front()
        
        stop()
        comm1.write(b'give_d')

finally:
    GPIO.cleanup()
    comm1.close()
        
