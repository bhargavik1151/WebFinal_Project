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


@app.post("/customers/")
def create_customer(customer: Customer):
    if customer.cust_id is not None:
        raise HTTPException(status_code=400, detail="cust_id cannot be set on POST request")

    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?);", (customer.name, customer.phone))
    customer.cust_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return customer

@app.get("/customers/{cust_id}")
def read_customer(cust_id: int):
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM customers WHERE id=?", (cust_id,))
    customer = cursor.fetchone()
    conn.close()
    if customer is not None:
        return Customer(cust_id=customer[0], name=customer[1], phone=customer[2])
    else:
        raise HTTPException(status_code=404, detail="Customer not found")



@app.put("/customers/{cust_id}")
def update_customer(cust_id: int, customer: Customer):
    # Check if customer ID provided in the path matches

    # Update logic changed here: 
    # Instead of updating all fields, lets allow partial updates based on provided data
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()

    # Check if the customer ID exists in the database
    cursor.execute("SELECT id FROM customers WHERE id = ?;", (cust_id,))
    existing_customer = cursor.fetchone()
    if existing_customer is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer ID not found")

    # Build update query based on provided data in customer object
    update_query = "UPDATE customers SET "
    update_data = []
    if customer.name is not None:
        update_query += "name=?, "
        update_data.append(customer.name)
    if customer.phone is not None:
        update_query += "phone=? "
        update_data.append(customer.phone)

    # Remove trailing comma if only one field is updated
    update_query = update_query.rstrip(", ") + " WHERE id=?; "
    update_data.append(cust_id)

    # Execute update query with parameters
    cursor.execute(update_query, update_data)
    conn.commit()

    # Re-fetch the updated customer data
    cursor.execute("SELECT id, name, phone FROM customers WHERE id=?", (cust_id,))
    updated_customer = cursor.fetchone()

    # Close the connection after all operations are completed
    conn.close()

    # Return the updated customer information
    if updated_customer is not None:
        return Customer(cust_id=updated_customer[0], name=updated_customer[1], phone=updated_customer[2])
    else:
        # This shouldn't happen, but handle potential error
        raise HTTPException(status_code=500, detail="Internal server error during update")



