# Initialize the backend app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
from flask_login import LoginManager, login_manager



app = Flask(__name__, static_folder='./static')

# connect the database using sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SECRET_KEY'] = '5e85752d580a74b6f80231020d3f2e95'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Ldy26060@localhost:3306/tripnow'

db = SQLAlchemy(app)


app.config.from_object(__name__)
# Request
CORS(app, resources={r'/*': {'origins': '*'}})


from trip import routes

 

