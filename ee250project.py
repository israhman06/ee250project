from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan

dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor

setRGB(0,255,0)

while True:
	try:
		[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
		print("temp =", temp, "C\thumidity =", hum,"%")
		t = str(temp)
		h = str(hum)
		
		setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")
		if (temp>20):
			print ("Hot")
			setRGB(255,0,0)
		else:
			print ("Cold")
			setRGB(0,0,255)
