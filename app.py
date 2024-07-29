# app.py
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    con = sqlite3.connect('superstore.db')
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    product_name = request.args.get('name')
    if not product_name:
        return render_template('search.html', products=[])

    products = query_db('SELECT * FROM products WHERE name LIKE ?', ('%' + product_name + '%',))
    return render_template('search.html', products=products)

@app.route('/order', methods=['POST'])
def order():
    product_code = request.form.get('product_code')
    quantity = int(request.form.get('quantity'))

    if not product_code or not quantity:
        return redirect(url_for('index'))

    product = query_db('SELECT * FROM products WHERE product_code = ?', (product_code,), one=True)
    if not product:
        return render_template('order.html', message='Product not found.')

    if product[4] < quantity:
        return render_template('order.html', message='Not enough stock available.')

    # Update stock
    new_stock = product[4] - quantity
    con = sqlite3.connect('superstore.db')
    cur = con.cursor()
    cur.execute('UPDATE products SET stock = ? WHERE product_code = ?', (new_stock, product_code))
    con.commit()
    cur.close()
    con.close()

    return render_template('order.html', message='Order placed successfully.')

if __name__ == '__main__':
    app.run(debug=True)
