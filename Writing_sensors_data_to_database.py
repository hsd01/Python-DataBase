"""#########################################################
    Make sure to import GPIO of RPi and set it as u want:
    and make sure u run create_table() function only once
    conn = sqlite3.connect('c:/Users/Taka/Desktop/Sensor_1.db')=> c:/Users/Taka/Desktop/Sensor_1.db is the path
    for RPi path can be anywhere u want to create .db file like /home/pi/Desktop etc u got the point
    sensor_data_entry() will write the data to DB, but make sure to change SR_No, Sensor, value. to ADC value of ur sensor
    srno takes real no. sensor take text or string its on u, value is for sensor data int

    The two function one will createdatabase and other will write values to database

                                                                                Regards
                                                                                Hemant S D
    
"""

import sqlite3
import time
import datetime


conn = sqlite3.connect('c:/Users/Taka/Desktop/Sensor_1.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS MySensorData(SR_No REAL, Sensor TEXT, value REAL)")



def sensor_data_entry():

    SR_No = 1
    Sensor = 'LM35'
    value = random.randrange(0,10)

    c.execute("INSERT INTO MySensorData (SR_No, Sensor, value) VALUES (?, ?, ?)",
          (SR_No, Sensor, value))

    conn.commit()

