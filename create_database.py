# create_database.py
import sqlite3

conn = sqlite3.connect('superstore.db')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_code TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
''')

# Sample data
products = [
    ('M001', 'iPhone 14', 'Smartphone', 10999, 50),
    ('M003', 'Google Pixel 7', 'Smartphone', 89999, 100),
    ('M005', 'Xiaomi Mi 11', 'Smartphone', 79999, 60),
    ('M007', 'Huawei P50 Pro', 'Smartphone', 89999, 30),
    ('M009', 'Vivo X80 Pro', 'Smartphone', 96999, 25),
    ('M010', 'Asus ROG Phone 6', 'Smartphone', 99999, 45),
    ('M012', 'Realme GT 2 Pro', 'Smartphone', 79999, 65),
    ('M013', 'Motorola Edge 30', 'Smartphone', 69999, 85),
    ('M015', 'ZTE Axon 30 Ultra', 'Smartphone', 72999, 35),
    ('M020', 'Fairphone 4', 'Smartphone', 59999, 100),
]



c.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?)', products)

conn.commit()
conn.close()
