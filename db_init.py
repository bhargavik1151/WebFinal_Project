import sqlite3
import json
conn = sqlite3.connect("db.sqlite")
curr = conn.cursor()

curr.execute("""
             CREATE TABLE customers(
             id INTEGER PRIMARY KEY,
             name CHAR(64),
             phone CHAR(10)
             );
             """
             )




curr.execute(
    """
    CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name CHAR(64),
    price REAL
    );
"""
)


curr.execute(
    """
CREATE TABLE orders (
id INTEGER PRIMARY KEY,
notes TEXT,
cust_id INTEGER,
timestamp INTEGER,
FOREIGN KEY(cust_id) REFERENCES customers(id)
);
"""
)

