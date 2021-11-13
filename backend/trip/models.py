from trip import app, db, ma
from marshmallow import fields


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,

        }
    # def __repr__(self, users=None):
    #     if not users:
    #         return 404
    #     res = []
    #     for item in users:
    #         res.append(
    #             {
    #                 'id': item.id,
    #                 'user_name': item.user_name,
    #                 'phone': item.phone,
    #                 'email': item.email,
    #                 'password': item.password
    #             }
    #         )
    #     return res
    # def __repr__(self):
    #     return '<Product %d>' % self.id


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = fields.Number(dump_only=True)
    user_name = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)


