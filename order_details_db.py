# from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import SqliteDatabase, Model, CharField, FloatField, DateTimeField, PrimaryKeyField, ForeignKeyField
from datetime import datetime
from products_db import Product
from order_db import Order

# Configure the SQLite database
db = SqliteDatabase('instance/order_details.db')

# Define a Peewee model for order details
  
class OrderDetail(Model):
    order_detail_id = PrimaryKeyField(unique=True, null=False)
    order_id = ForeignKeyField(Order, backref='order_details')
    product_id = ForeignKeyField(Product)
    address = CharField()
    pincode = CharField()
    city = CharField()
    contact_no = CharField()

    class Meta:
        database=db
    




# class OrderDetail(Model):
#     order_detail_id = PrimaryKeyField(unique=True, null=False)
#     order_id = ForeignKeyField(Order, backref='order_details')
#     address = CharField()
#     pincode = CharField()
#     city = CharField()
#     contact_no = CharField()

#     class Meta:
#         database = db

db.connect()
db.create_tables([OrderDetail], safe=True)
