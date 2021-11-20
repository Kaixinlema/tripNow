from flask_login.mixins import UserMixin
from trip import app, db
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

class Hotel(db.Model):
    __tablename__ = "hotel_recommend"
    hotel_id = db.Column(db.Integer,primary_key=True,nullable=False)
    attraction_id = db.Column(db.Integer)
    type = db.Column(db.Integer)
    name = db.Column(db.String(30))
    score = db.Column(db.Float)
    price = db.Column(db.Integer)
    distance = db.Column(db.String(10))

    def to_json(self):
        return{
            'attraction_id': self.attraction_id, 
            'type': self.type, 
            'name': self.name,
            'score': self.score,
            'price': self.price,
            'distance': self.distance,
        }

class Rule(db.Model):
    __tablename__ = "association_rule"
    rule_id = db.Column(db.Integer,primary_key=True,nullable=False)
    antecents = db.Column(db.String(20))
    consequents = db.Column(db.String(20))
    support = db.Column(db.Float)
    confidence = db.Column(db.Float)
    lift = db.Column(db.Float)

    def to_json(self):
        return{
            'rule_id': self.rule_id,
            'antecents': self.antecents,
            'consequents': self.consequents
        }
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
    attraction_time = db.Column(db.Integer)
    attraction_cost = db.Column(db.Integer)
    attraction_detail = db.Column(db.Text)
    def to_json(self):
        return {
            'id': self.id,
            'attraction_name': self.attraction_name,
            'attraction_label': self.attraction_label,
            'attraction_lng': self.attraction_lng,
            'attraction_lat': self.attraction_lat,
            'attraction_time': self.attraction_time,
            'attraction_cost': self.attraction_cost,
            'attraction_detail': self.attraction_detail,
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


