import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser


conn = sqlite3.connect('c:/Users/Taka/Desktop/Car_1.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS MySensorData(SR_No REAL, car TEXT, reg REAL)")



def dynamic_data_entry():

    SR_No = 1
    Sensor = 'LM35'
    value = random.randrange(0,10)

    c.execute("INSERT INTO MySensorData (SR_No, Sensor, value) VALUES (?, ?, ?)",
          (SR_No, Sensor, value))

    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM MySensorData')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)
            
def graph_data():
    c.execute('SELECT datestamp, value FROM MySensorData')
    data = c.fetchall()

    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()    



create_table()
#dynamic_data_entry()
#read_from_db()


c.close
conn.close()
