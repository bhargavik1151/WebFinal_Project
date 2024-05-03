from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import time

# Initialize FastAPI app
app = FastAPI()
# Define models
class Customer(BaseModel):
    cust_id: int | None = None
    name: str
    phone: str

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float

class Order(BaseModel):
    order_id: int | None = None
    notes: str
    cust_id: int
    timestamp: int

# Database connection and foreign key support
conn = sqlite3.connect("db.sqlite")
conn.execute("PRAGMA foreign_keys = ON;")
conn.close()
