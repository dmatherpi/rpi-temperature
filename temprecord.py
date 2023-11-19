#   Temperature Sensor Data Recorder
#   Author: dmatherpi

#-----Notes
#   Code written in Python to run on Raspberry Pi's with a temperature sensor connected via GPIO
#   This code records the data from a Digital Temperature Sensor DS18B20 and saves the information locally to a text file
#   Replace line 27 address with the address to your local temperature sensor
#   Replace line 65 address with the file path and name of the file to save the data too. This is a dedicated text file.

#-----Initialise the System and all loads required
#-*- coding: utf-8 -*-
print ("auto_temprecord_hourly.py starting")
print ("Program will measure the temperature, record the temperature locally in text file")
print ("Importing os")
import os
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

print ("Importing time")
import time

print ("Importing datetime")
import datetime

#------Define the temperature sensors

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

print ("current temperature = " + str(read_temp1()) + " degrees Celcius")

#-----Write to txt file
    text_file = open("/home/pi/temp_record.txt", "a")  
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
    text_file.write(str(read_date()) + ", ")
    text_file.write(str(read_time()) + ", ")
    text_file.write("Temperature 1, " + str(read_temp1()) + ", \n")
    text_file.close()
    print ("file updated and data saved")

print ("The script is complete")
