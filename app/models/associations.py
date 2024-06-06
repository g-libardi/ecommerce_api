from sqlalchemy import Column, Integer, String, ForeignKey, Table
from app.extensions import db

product_category = Table('product_category', db.Model.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)

order_items = Table('order_items', db.Model.metadata,
    Column('order_id', Integer, ForeignKey('order.id')),
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('quantity', Integer)
)
