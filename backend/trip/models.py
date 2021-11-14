from flask_login.mixins import UserMixin
from trip import app, db
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

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


