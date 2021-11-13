from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Ldy26060@localhost:3306/tripnow'
    # 协议：mysql+pymysql
    # 用户名：root
    # 密码：2333
    # IP地址：localhost
    # 端口：3306
    # 数据库名：runoob #这里的数据库需要提前建好
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
   
    def __init__(self, user_name, phone, email, password):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.password = password


    def __repr__(self):
        return '<Product %d>' % self.id
