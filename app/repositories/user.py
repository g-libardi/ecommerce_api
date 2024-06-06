from ..models import User
from ..extensions import db

class UserRep:
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def create(username, password, first_name, last_name):
        user = User(username=username, password=password, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def delete(id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user
    