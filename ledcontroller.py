import RPi.GPIO as GPIO
from tkinter import Tk, Scale, HORIZONTAL

# GPIO setup using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the LEDs
RED_LED_PIN = 17   
GREEN_LED_PIN = 27 
WHITE_LED_PIN = 22 

# Set the GPIO pins as outputs
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(WHITE_LED_PIN, GPIO.OUT)

# Setup PWM for LEDs (1000 Hz)
red_pwm = GPIO.PWM(RED_LED_PIN, 1000)
green_pwm = GPIO.PWM(GREEN_LED_PIN, 1000)
white_pwm = GPIO.PWM(WHITE_LED_PIN, 1000)

# Start PWM with 0% duty cycle (LEDs off)
red_pwm.start(0)
green_pwm.start(0)
white_pwm.start(0)

# Update red LED brightness
def update_red_led(value):
    red_pwm.ChangeDutyCycle(int(value))

# Update green LED brightness
def update_green_led(value):
    green_pwm.ChangeDutyCycle(int(value))

# Update white LED brightness
def update_white_led(value):
    white_pwm.ChangeDutyCycle(int(value))

# Tkinter window setup
root = Tk()
root.title("LED Brightness Control")

# Sliders for controlling LED brightness
red_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Red LED", command=update_red_led)
red_slider.pack()

green_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Green LED", command=update_green_led)
green_slider.pack()

white_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="White LED", command=update_white_led)
white_slider.pack()

# Start Tkinter event loop
root.mainloop()

# Stop PWM and cleanup GPIO on exit
red_pwm.stop()
green_pwm.stop()
white_pwm.stop()
GPIO.cleanup()
