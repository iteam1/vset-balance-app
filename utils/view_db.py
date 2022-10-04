import os 
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect('./root/site.db') # Create the connection to the database
c = conn.cursor() # Create the cursor for the connection
print('database connected!')

id =1

column_list = ['id','balance_name','balance_value','printer_name']
print("Start reading robot id = {id}")

if __name__ == "__main__":
    
    while True:
        
        c.execute(f"""SELECT *FROM db WHERE id = {id}""")
        conn.commit()
        data = c.fetchone()
        message = str(datetime.now()) + "\n{\n" 
        for i in range(len(data)):
            if i == len(data) - 1:
                message = message + column_list[i] + ' = ' + str(data[i])
            else:
                message = message + column_list[i] + ' = ' + str(data[i]) + ', \n'
        
        message = message + "\n}\n"
        
        print(message)
        
        time.sleep(0.1)
        
        os.system('clear')
    
    conn.close()