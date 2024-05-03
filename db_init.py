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
