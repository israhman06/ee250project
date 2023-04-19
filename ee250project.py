import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import sys
import grovepi
from grove_rgb_lcd import *


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SPI_PORT=0
SPI_DEVICE = 0

#mcp = Adafruit_MCP3008.MCP3008(spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE))

temperaturePin = 0 #Temp sensor connected to A0
   
if __name__ == '__main__':
	while (True):
		temperatureVal = grovepi.temp(temperaturePin)
		print("temp =", temperatureVal)
        time.sleep(.5)