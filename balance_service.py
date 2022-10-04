import serial
import sqlite3
import time
import requests
import json

conn = sqlite3.connect("./root/site.db")
c = conn.cursor()
query_string = '''UPDATE db
                    SET balance_value = ?
                    WHERE id = ?'''

# input com port
my_com = input("Enter your serial-com (Default COM3): ") 
if my_com == "": my_com = "COM3"

try:
    my_serial = serial.Serial(my_com)
    print(f"Serial COM = {my_serial.name} Connected!") # check com port
except Exception as e:
    print(e)
    exit() # exit if error

class mybalance():
    def __init__(self,conn =conn):
        self.conn = conn
        
    def update_value(self,query,value):
        c = self.conn.cursor()
        c.execute(query,[value,1])
        self.conn.commit()
        
the_balance = mybalance(conn = conn)

value = 0.0
base_url = 'https://vset.vvs.vn/parse/classes/GoldWeight/IXvPHGKTen'
data = {"value":value}
headers = {
    'X-Parse-Application-Id':'SCWASRTWK1Y9AVMP1KFC',
}

def update_api(value):
    with requests.Session() as s:
        data = {"value":float(value)}
        res = s.put(base_url,headers=headers,data=json.dumps(data))
        print(res.json())
    
if __name__ == "__main__":
    while True:
        comming_data = my_serial.read(14) # read():read on byte, read(14): read up to 14 bytes, readline() readline
        my_string = comming_data.decode()
        value = my_string.strip().split("T")[0]
        print(f"value: {value}")
        the_balance.update_value(query_string,my_string)
        update_api(value)
        time.sleep(0.1)