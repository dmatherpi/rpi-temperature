#	Temperature Sensor Data Read Out and Report
#	Author: dmatherpi

#-----Notes
#   Code written in Python to run on Raspberry Pi's with a temperature sensor connected via GPIO
#   This code records the data from a Digital Temperature Sensor DS18B20 and reports the temperature in Celsius when run as a script either locally or via SSH.
#   Replace the address in line 20 with the address to your local temperature sensor

#-----Initialise the System and load the GPIO modprobe

import os
import time
import datetime
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
#-*- coding: utf-8 -*-

#------Define the temperature sensor

temp_sensor1 = '/sys/bus/w1/devices/28-0414684b00ff/w1_slave'

#------Read Temperature Sensor 1 (temp_sensor1)

def temp_raw1():
    f = open(temp_sensor1, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp1():
    lines = temp_raw1()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw1()
    temp_output1 = lines[1].find('t=')
    if temp_output1 != -1:
        temp_string1 = lines[1][temp_output1+2:]
        temp_c1 = float(temp_string1) / 1000
        return temp_c1
	
#-----Read Current Time

def read_date():
	import time
	ts = time.time()
	stdate = datetime.date.fromtimestamp(ts).strftime('%d-%m-%Y')
	current_date = str(stdate)
	return current_date

def read_time():
	import time
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
	current_time = str(st)
	return current_time

print (str(read_temp1()))




    


	


