from ..models.product import Product
from ..extensions import db

class ProductRep:
    @staticmethod
    def get_all():
        return Product.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)
    
    @staticmethod
    def create(name, price, categories_ids, description=None, stock=0):
        product = Product(name=name, price=price, description=description, stock=stock)
        for category_id in categories_ids:
            product.categories.append(category_id)
        db.session.add(product)
        db.session.commit()
        return product
    
    @staticmethod
    def delete(id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return product