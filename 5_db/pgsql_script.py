import sqlite3

conn = sqlite3.connect('lite.db')
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

def insert(item, quantity, price):
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

def view():
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    return rows

def delete(item):
    # !: "," must be existing after "item"
    # !  when there is only ONE single item in a set
    cur.execute('DELETE FROM store WHERE item=?', (item,))

def update(item, quantity, price):
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))

print(view())

conn.commit()
conn.close()