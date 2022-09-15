#RaspberryPi py file
import RPi.GPIO

# GPIO pin assignments.
HUB75E_R1 = 27
HUB75E_G1 = 25
HUB75E_B1 = 22
HUB75E_R2 = 5
HUB75E_G2 = 12
HUB75E_B2 = 16

HUB75E_A = 20
HUB75E_B = 21
HUB75E_C = 6

HUB75E_CLK = 13
HUB75E_LAT = 19
HUB75E_OE = 26

LOW = 0
HIGH = 1

def DisplayInit():
    # Configure GPIO pins.
    RPi.GPIO.setwarnings(False)
    RPi.GPIO.setmode(RPi.GPIO.BCM)
    RPi.GPIO.setup(HUB75E_R1, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_G1, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_B1, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_R2, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_G2, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_B2, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_A, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_B, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_C, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_CLK, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_LAT, RPi.GPIO.OUT, initial=0)
    RPi.GPIO.setup(HUB75E_OE, RPi.GPIO.OUT, initial=0)
    
def CLK_HIGH():
    RPi.GPIO.output(HUB75E_CLK, HIGH)
    
def CLK_LOW():
    RPi.GPIO.output(HUB75E_CLK, LOW)
    
def LAT_HIGH():
    RPi.GPIO.output(HUB75E_LAT, HIGH)
    
def LAT_LOW():
    RPi.GPIO.output(HUB75E_LAT, LOW)
    
def OE_HIGH():
    RPi.GPIO.output(HUB75E_OE, HIGH)
    
def OE_LOW():
    RPi.GPIO.output(HUB75E_OE, LOW)
    
def SET_R1(output_value):
    RPi.GPIO.output(HUB75E_R1, output_value)

def SET_G1(output_value):
    RPi.GPIO.output(HUB75E_G1, output_value)
    
def SET_B1(output_value):
    RPi.GPIO.output(HUB75E_B1, output_value)
    
def SET_R2(output_value):
    RPi.GPIO.output(HUB75E_R2, output_value)
    
def SET_G2(output_value):
    RPi.GPIO.output(HUB75E_G2, output_value)
    
def SET_B2(output_value):
    RPi.GPIO.output(HUB75E_B2, output_value)
    
def SET_A(output_value):
    RPi.GPIO.output(A_IO,output_value)
    
def SET_B(output_value):
    RPi.GPIO.output(B_IO,output_value)
    
def SET_C(output_value):
    RPi.GPIO.output(C_IO,output_value)
