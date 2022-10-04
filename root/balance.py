import sqlite3

conn = sqlite3.connect("./root/site.db")
c = conn.cursor()

class mybalance():
    
    def __init__(self,conn =conn):
        self.conn = conn
    
    def read_value(self):
        c = self.conn.cursor()
        c.execute("""SELECT *FROM db WHERE id = 1""")
        data = self.c.fetchone() # Get all row
        self.conn.commit()
        balance_value = data[2]
        return balance_value
    
    
  
        