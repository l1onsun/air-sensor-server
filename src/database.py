import sqlite3 as sql

con = sql.connect("database.db")
cur = con.cursor()

# cur.execute()
# cur.execute(""" INSERT INTO info VALUES(?,?,?,?)""", (str(date), temp, co2, humi))
con.close()
