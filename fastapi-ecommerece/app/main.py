from fastapi import FastAPI
from typing import List
from services.products import Product

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

products_list = [
        Product(name="Laptop",price=999.99,in_stock=True,quantity=10,description="High-performance laptop"),
        Product(name="Smartphone",price=699.99,in_stock=True,quantity=25,description="Latest smartphone")
    ]

# Get method
# for get all products
@app.get("/products")
def get_all_products():
    return products_list


# for getting a single perticular product.
@app.get("/products/{product_name}")
def get_product_by_name(product_name: str):
    for product in products_list:
        if product.name == product_name:
            return product
    return {"message": "Product not found"}

# Post method to add a new product.
@app.post("/products")
def add_product(product : Product):
    products_list.append(product)
    return {"message" : "Product added Successfully"}

#  Put method to update an existing product.
@app.put("/products/{product_name}")
def update_product(product_name: str, update_product :Product):
    for i in range(len(products_list)):
        if products_list[i].name ==product_name:
            products_list[i] = update_product
            return {"message" : "Product Update Successfully"}
        return {"message" : "Product Not Found"}

# Delete method for deleting a product.
@app.delete("/products/{product_name}")
def delete_product(product_name: str):
    for i in range(len(products_list)):
        if products_list[i].name == product_name:
            del products_list[i]
            return {"message" : "Prodcut Deleted Successfully"}
        return {"message" : "Product Not Found"}
    

