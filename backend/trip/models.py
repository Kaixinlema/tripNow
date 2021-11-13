from trip import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self, users=None):
        if not users: 
            return 404
        res=[]
        for item in users:
            res.append({
                'id': item.id,
                'user_name': item.user_name,
                'phone': item.phone,
                'email': item.email,
                'password': item.password
            })
        return res
