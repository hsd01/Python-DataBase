import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('c:/Users/Taka/Desktop/Sensor.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS MySensorData(SR_No REAL, Name_Sensor TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO MySensorData VALUES(1,'Python',666)")
    
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

    
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
create_table()
data_entry()

c.close
conn.close()
