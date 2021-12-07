import sqlite3

from sqlalchemy import create_engine

e = create_engine("sqlite:///Products.db")
conn = sqlite3.connect("Products.db")
cursor = conn.cursor()


def insert():
    name = input('Name\n')
    price = float(input("Price\n"))
    quantity = int(input("Quantity\n"))
    comment = input("Comment\n")
    e.execute('''INSERT INTO Products(name, price, quantity, comment) VALUES (?, ?, ?, ?)''',
              (name, price, quantity, comment))
    conn.commit()
    conn.commit()


def read():
    records = cursor.execute("SELECT * FROM Products")
    ls = cursor.fetchall()
    for i in ls:
        print(i, end='\n')


def update_by_id(dev_id, quantity):
    sql_update_query = """Update Products set quantity = ? where id = ?"""
    data = (quantity, dev_id)
    cursor.execute(sql_update_query, data)
    conn.commit()
    print("Post updated")


def delete_by_id(id):
    cursor.execute('DELETE FROM Products WHERE id = ?', (id,))
    conn.commit()
