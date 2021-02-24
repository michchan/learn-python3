import psycopg2

conn = psycopg2.connect("dbname='db1_py' user='postgres' password='postgres' host='localhost' port=15432")
cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

def insert(item, quantity, price):
    cur.execute("INSERT INTO store (item, quantity, price) VALUES (%s, %s, %s)", (item, quantity, price))

def view():
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    return rows

def delete(item):
    # !: "," must be existing after "item"
    # !  when there is only ONE single item in a set
    cur.execute('DELETE FROM store WHERE item=%s', (item,))

def update(item, quantity, price):
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))

# create_table()
# insert('toDelete', 8, 23)
# delete('toDelete')
# update('Orange', 40, 13)
print(view())

conn.commit()
conn.close()