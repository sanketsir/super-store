# verify_database.py
import sqlite3

conn = sqlite3.connect('superstore.db')
c = conn.cursor()

c.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="products"')
table_exists = c.fetchone()

if table_exists:
    c.execute('SELECT * FROM products')
    rows = c.fetchall()
    for row in rows:
        print(row)
else:
    print("Table 'products' does not exist.")

conn.close()
