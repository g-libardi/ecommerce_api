from ..models.order import Order
from ..extensions import db

class OrderRep:
    @staticmethod
    def get_all():
        return Order.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Order.query.get(id)
    
    @staticmethod
    def create(total, status, customer_id, items):
        order = Order(total=total, status=status, customer_id=customer_id)
        for item in items:
            order.items.append(item)
        db.session.add(order)
        db.session.commit()
        return order
    
    @staticmethod
    def update(id, total, status, customer_id, items):
        order = Order.query.get(id)
        order.total = total
        order.status = status
        order.customer_id = customer_id
        order.items = items
        db.session.commit()
        return order
    
    @staticmethod
    def delete(id):
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return order