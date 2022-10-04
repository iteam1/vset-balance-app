'''
Run this command outside /root
'''
import sqlite3 

balance_name = "Shimadzu ATY224R"
balance_value  = "not available"
printer_name = "Xprinter XP-350BM"
row = (balance_name,balance_value ,printer_name)

conn = sqlite3.connect("./root/site.db")
c = conn.cursor()

query_string = '''INSERT INTO db(balance_name,balance_value ,printer_name)
              VALUES(?,?,?) '''

c.execute("""
          CREATE TABLE db (
              id INTEGER PRIMARY KEY,
              balance_name TEXT, 
              balance_value TEXT,
              printer_name TEXT
              )
              """)

c.execute(query_string,row)

conn.commit()

print('Database created!')

conn.close()