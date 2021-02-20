import RPi.GPIO as gpio
import time
import os


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#gpio_setup
gpio.setup(4,gpio.OUT)
gpio.setup(15,gpio.IN,pull_up_down = gpio.PUD_UP)

#pwn_setup
pin = gpio.PWM(4,100)
pin.start(0)

try:

    while True:
        
        if gpio.input(15) == 0:
            time.sleep(0.8)
            if gpio.input(15):
                #playaudiofile
                os.system("sudo mpg123 /home/pi/iron-man-repulsor.mp3 &")

                print(gpio.input(15))
                x = 0
                while x < 75:
            
                    x = x + 1
                    pin.ChangeDutyCycle(x)
                    time.sleep(0.0052)



                for i in range(74,100):
                    pin.ChangeDutyCycle(i)
                    time.sleep(0.00134)

                for o in range(100):
                    pin.ChangeDutyCycle(99 - o)
                    time.sleep(0.005)

            elif gpio.input(15) == 0:
                gpio.cleanup()
                os.system("sudo shutdown -h now")

            

finally:
    print("done")
    gpio.cleanup()
