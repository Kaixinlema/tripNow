from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object(__name__)

# 跨域请求
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SECRET_KEY'] = '5e85752d580a74b6f80231020d3f2e95'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Ldy26060@localhost:3306/tripnow'

db = SQLAlchemy(app)
 # 添加到db = SQLAlchemy(app)后面

from trip import routes

 

