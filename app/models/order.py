from ..extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship('Customer', back_populates='orders')
    items = db.relationship('OrderItem', back_populates='order', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'Order {self.id}'