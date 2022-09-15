#displayDriver.py file
from DriverTypedef import *
from RaspberryPi import *
import RPi.GPIO as GPIO
import time
import random
import _thread
from colors import *

#constants
DISPLAY_WIDTH = 64
DISPLAY_HEIGHT = 32

PANEL_WIDTH = 32
PANEL_HEIGHT = 32
NUM_OF_SELECTION_BITS = 3
NUM_OF_SUBPANELS = 2

NUM_OF_PANELS_X = int(DISPLAY_WIDTH/PANEL_WIDTH)
NUM_OF_PANELS_Y = int(DISPLAY_HEIGHT/PANEL_HEIGHT)
NUM_OF_PANELS = (NUM_OF_PANELS_X*NUM_OF_PANELS_Y)
NUM_PIXELS_PER_PANEL = (PANEL_WIDTH*PANEL_HEIGHT)
NUM_OF_ROWS = (1<<NUM_OF_SELECTION_BITS)
NUM_OF_COLUMNS = PANEL_WIDTH
NUM_OF_SEGMENTS = (int(PANEL_HEIGHT/NUM_OF_SUBPANELS)>>NUM_OF_SELECTION_BITS)
SUBPANEL_OFFSET = (DISPLAY_WIDTH*(PANEL_HEIGHT/NUM_OF_SUBPANELS))
VERTICAL_PANEL_OFFSET = (DISPLAY_WIDTH*PANEL_HEIGHT)
SEGMENT_OFFSET = (DISPLAY_WIDTH<<NUM_OF_SELECTION_BITS)

DOWN  = 0x01
UP    = 0x02
RIGHT = 0x04
LEFT  = 0x08

X_AXIS = 1
Y_AXIS = 2

BMP_DIB = 0x0E
BMP_WIDTH = 0x12
BMP_HEIGHT = 0x16
BMP_BPP = 0x1C
BMP_COLORS = 0x2E

DEFAULT_FORMAT = 2
PPB = 1
BPC = 5
chMask = 0x1F
InitFlag = 0

#variables
BitsPerChannel = int(BPC)
Brightness = int(20)
PositionX = int(0)
PositionY = int(0)
FRAME_BUFF = [color565_t(0,0,0,0) for i in range(2048)]

def Clock():
    CLK_HIGH()
    CLK_LOW()
    
def Latch():
    LAT_HIGH()
    LAT_LOW()
  
def delay_nops(nops):
    while nops > 0:
        nops = nops - 1
        #do nothing

  
def selectRow(x):
    RPi.GPIO.output(HUB75E_A, (x&0x01))
    RPi.GPIO.output(HUB75E_B, ((x&0x02)>>1))
    RPi.GPIO.output(HUB75E_C, ((x&0x04)>>2))
    
def rCh(c):
    ret_color = c.color>>11
    return ret_color
    
def gCh(c):
    ret_color = c.color>>6
    return ret_color
    
def bCh(c):
    ret_color = c.color
    return ret_color    
    
def getFRAMEpx(i):
    return FRAME_BUFF[i]

def setFRAMEpx(i,v):
    FRAME_BUFF[i].r = v.r
    FRAME_BUFF[i].g = v.g
    FRAME_BUFF[i].b = v.b
    FRAME_BUFF[i].color = v.color
    
# def displayFRAMEbuff():
#     for i in range(2048):
#         print(FRAME_BUFF[i])
    
def COLOR(c):    
    b = ((c&0x0000FF)>>3)
    g = (((c&0x00FF00)>>8)>>2)
    r = (((c&0xFF0000)>>16)>>3)
    temp_r = ((r<<11)&0xF100)
    temp_g = ((g<<5)&0x07E0)
    temp_b = (b&0x1F)
    color = (temp_r|temp_g|temp_b)
    boja = color565_t(b,g,r,color)
    return boja
    
def setColor(px,i):

    SET_R1(rCh(getFRAMEpx(px))>>i)
    SET_G1(gCh(getFRAMEpx(px))>>i)
    SET_B1(bCh(getFRAMEpx(px))>>i)
    
    px = px + SUBPANEL_OFFSET
    px = int(px)

    SET_R2(rCh(getFRAMEpx(px))>>i)
    SET_G2(gCh(getFRAMEpx(px))>>i)
    SET_B2(bCh(getFRAMEpx(px))>>i)

    
def displayClear():
    displayFill(COLOR(0))
    
def displayFill(color):
    for i in range(NUM_OF_PANELS*NUM_PIXELS_PER_PANEL):
        setFRAMEpx(i, color)
        
def refreshDisplay():

    for cBit in range(BitsPerChannel):
        for row in range(NUM_OF_ROWS):
            selectRow(row)
            y_offset = row*DISPLAY_WIDTH
            for panel_y in range(NUM_OF_PANELS_Y):
                x_offset = 0
                for panel_x in range(NUM_OF_PANELS_X):
                    for segment in range(1,NUM_OF_SEGMENTS):
                        pixel=y_offset+x_offset+((NUM_OF_SEGMENTS-segment)*SEGMENT_OFFSET)
                        for column in range(PANEL_WIDTH):
                            setColor(pixel + column, cBit)
                            Clock()
                    x_offset = x_offset + PANEL_WIDTH
                y_offset = y_offset + VERTICAL_PANEL_OFFSET
            Latch()
                
            OE_LOW()
            delay_nops(Brightness<<cBit)
            OE_HIGH()
            delay_nops(1)
            
def displayGoTo(x,y):
    x = x%DISPLAY_WIDTH
    y = y%DISPLAY_HEIGHT
    PositionX = x
    PositionY = y
    
def displaySetPixel(x,y,color):
    x = x%DISPLAY_WIDTH
    y = y%DISPLAY_HEIGHT
    
    setFRAMEpx(x+y*DISPLAY_WIDTH, color)
            
def displayDrawRectangle(width, height, line_color, fill_color):
    x1 = PositionX
    y1 = PositionY
    
    for x in range(width+1):
        displaySetPixel(x1+x,y1,line_color)
        displaySetPixel(x1+x,y1+height,line_color)
        
    for y in range(height+1):
        displaySetPixel(x1, y1+y, line_color)
        displaySetPixel(x1+width, y1+y, line_color)

    for x in range(1,width):
        for y in range(1,height):
            displaySetPixel(x1+x, y1+y, fill_color)
    
def InitTask():
    InitFlag = 1
    DisplayInit()
    #displayDrawRectangle(10,15,COLOR(BLUE),COLOR(GREEN))
    displayFill(COLOR(BLUE))
    
InitTask()
while True:
    refreshDisplay()
    time.sleep(0.005)








                        


    
