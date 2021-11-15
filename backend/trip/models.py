from flask_login.mixins import UserMixin
from trip import app, db
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

class Label(db.Model):
    __tablename__ = "attraction_label"
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    label_name = db.Column(db.String(10))

    def to_json(self):
        return {
            'id': self.id,
        }

class Attraction(db.Model):
    __tablename__ = "attraction_info"
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    attraction_name = db.Column(db.String(20), nullable=False)
    attraction_label = db.Column(db.Integer,nullable=False)
    attraction_lng = db.Column(db.Float,nullable=False)
    attraction_lat = db.Column(db.Float,nullable=False)
    attraction_detail = db.Column(db.Text,nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'attraction_name': self.attraction_name,
            'attraction_label': self.attraction_label,
            'attraction_lng': self.attraction_lng,
            'attraction_lat': self.attraction_lat,
            'attraction_detail': self.attraction_detail
        }
    def basic_to_json(self):
        return {
            'id': self.id,
            'attraction_name': self.attraction_name,
            'attraction_label': self.attraction_label,
            'attraction_detail': self.attraction_detail
        }
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,

        }

class CalendarAdmin(UserMixin):
    """User class for flask-login"""

    def __init__(self, phone):
        self.phone = phone
        user = db.session.query(User).filter(User.phone==phone).one()
        self.name = user.user_name
        self.password = user.password
        self.id = user.id

# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         load_instance = True

#     id = fields.Number(dump_only=True)
#     user_name = fields.String(required=True)
#     phone = fields.String(required=True)
#     email = fields.String(required=True)
#     password = fields.String(required=True)


