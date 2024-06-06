from ..extensions import db
from ..models.category import Category

class CategoryRep:
    @staticmethod
    def get_all():
        return Category.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Category.query.get(id)
    
    @staticmethod
    def create(name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def update(id, name):
        category = Category.query.get(id)
        category.name = name
        db.session.commit()
        return category
    
    @staticmethod
    def delete(id):
        category = Category.query.get(id)
        db.session.delete(category)
        db.session.commit()
        return category
