import sqlite3
import psycopg2

# conn = sqlite3.connect("lite.db")
# cur = conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
# cur.execute("INSERT INTO store VALUES ('wine glass', 8, 10.5)")
# cur.execute("INSERT INTO store VALUES (?,?,?)",('water', 8, 10.5))
# cur.execute("SELECT * FROM store")
# rows = cur.fetchall()
# conn.commit()
# conn.close()

# cur.execute("DELETE * FROM store WHERE item=?",(item))
# cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))

# print(rows)

conn = psycopg2.connect("dbname = 'newone' user='postgres' password='postgres123' host='localhost' port='5432'")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('wine glass', 8, 10.5)")
# cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" %(item, quantity,price))
# cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item, quantity,price))
conn.commit()
conn.close()


