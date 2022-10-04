import serial
import sqlite3
import time

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
    
if __name__ == "__main__":
    while True:
        comming_data = my_serial.read(14) # read():read on byte, read(14): read up to 14 bytes, readline() readline
        my_string = comming_data.decode()
        print(my_string.strip())
        the_balance.update_value(query_string,my_string)
        time.sleep(0.1)