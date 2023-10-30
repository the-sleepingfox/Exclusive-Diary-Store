from peewee import SqliteDatabase, Model, CharField, FloatField, DateTimeField, PrimaryKeyField, ForeignKeyField
from datetime import datetime
from products_db import Product
from user_store_db import User

# Configure the SQLite database
db = SqliteDatabase('instance/order.db')

# Define a Peewee model for orders
class Order(Model):
    order_id= PrimaryKeyField(unique=True, null=False)
    user_id = ForeignKeyField(User.id, backref='orders')
    order_date = DateTimeField(default=datetime.now)
    order_amount = FloatField()
    
    class Meta:
        database=db
     
    # order_id= PrimaryKeyField(unique=True, null=False)
    # product_id = ForeignKeyField(Product, backref='orders')
    # order_date = DateTimeField(default=datetime.now)
    # order_amount = FloatField()

    # class Meta:
    #     database = db


db.connect()
db.create_tables([Order], safe=True)
