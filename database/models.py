from database.connection import db
from typing import List, Dict

class ProductModel:
    @classmethod
    def get_all(cls):
        return db.execute_query("SELECT * FROM products WHERE is_active = TRUE ORDER BY name")
    
    @classmethod
    def search(cls, term):
        query = "SELECT * FROM products WHERE name ILIKE %s OR code ILIKE %s LIMIT 50"
        return db.execute_query(query, (f"%{term}%", f"%{term}%"))

class CustomerModel:
    @classmethod
    def get_all(cls):
        return db.execute_query("SELECT * FROM customers WHERE is_active = TRUE ORDER BY name")

class WarehouseModel:
    @classmethod
    def get_all(cls):
        return db.execute_query("SELECT * FROM warehouses WHERE is_active = TRUE")
