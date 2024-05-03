# WebFinal_Project

# FastAPI CRUD Project

This project implements a simple CRUD (Create, Read, Update, Delete) API using FastAPI, SQLite, and Pydantic.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine
   
2. Install the required dependencies using pip

   pip install fastapi

   pip install pydantic
   
   pip install uvicorn

3. Run the db_init.py file.

4. Run the FastAPI application:

    uvicorn main:app

   
The API should now be running locally on `http://localhost:8000`.

## API Endpoints

### Customers

- `POST /customers/`: Create a new customer.
- `GET /customers/{cust_id}`: Retrieve a customer by ID.
- `PUT /customers/{cust_id}`: Update a customer by ID.
- `DELETE /customers/{cust_id}`: Delete a customer by ID.

### Items

- `POST /items/`: Create a new item.
- `GET /items/{item_id}`: Retrieve an item by ID.
- `PUT /items/{item_id}`: Update an item by ID.
- `DELETE /items/{item_id}`: Delete an item by ID.

### Orders

- `POST /orders/`: Create a new order.
- `GET /orders/{order_id}`: Retrieve an order by ID.
- `PUT /orders/{order_id}`: Update an order by ID.
- `DELETE /orders/{order_id}`: Delete an order by ID.

## Data Models

The API uses the following data models:

- `Customer`: Represents a customer with `cust_id`, `name`, and `phone` fields.
- `Item`: Represents an item with `id`, `name`, and `price` fields.
- `Order`: Represents an order with `order_id`, `notes`, `cust_id`, and `timestamp` fields.

## Database

The API uses SQLite as the database backend. The database file (`db.sqlite`) is created automatically when the application is run for the first time.




   



