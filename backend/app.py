from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import contextlib
import databases
import sqlalchemy

DATABASE_URL = "sqlite:///test.db"
engine = sqlalchemy.create_engine(DATABASE_URL, echo = True)

# create table
metadata = sqlalchemy.MetaData()
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("position", sqlalchemy.Integer),
)
metadata.create_all(engine)

# database connection

# list all products
def list_products(request):
    db_connection = engine.connect()
    query = products.select()
    results = db_connection.execute(query)
    products_list = []
    for item in results:
        t = {
            "type": item['type'],
            "title": item['title'],
            "position": item['position'],
        }
        products_list.append(t)
    return JSONResponse({'data': products_list})

# insert products to table
def insert_products(request):
    db_connection = engine.connect()
    data = request.json()
    inserted_product = products.insert().values(type = data['type'], title = data['title'], position = data['position'])
    result = db_connection.execute(inserted_product)
    
# update product
def update_product(request):
    db_connection = engine.connect()
    data = request.json()
    updated_product = products.update().where(products.c.id == data['id']).values(type = item['type'], title = item['title'], position = item['position'])
    result = db_connection.execute(updated_product)

# delete product
def delete_product(request):
    db_connection = engine.connect()
    data = request.json()
    deleted_product = products.delete().where(products.c.id == data['id'])
    result = db_connection.execute(deleted_product)


# url routes
routes = [
    Route('/', list_products, methods=['GET']),
    Route('/', insert_products, methods=['POST']),
    Route('/', update_product, methods=['PUT']),
    Route('/', delete_product, methods=['DELETE']),
]

# allow any domains and ports for CORS.
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
]


app = Starlette(debug=True, routes=routes, middleware=middleware)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
    