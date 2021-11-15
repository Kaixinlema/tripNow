from trip.models import *
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional
from flask_login import UserMixin
from trip import db

import pymysql


def User_query(phone,password):
    res = db.session.query(User).filter(User.phone==phone).filter(User.password==password).first()
    if res is not None:
        return res
class DatabaseOperations():
    # database connection
    __db_url = 'localhost'
    __db_username = 'root'
    __db_password = 'Ldy26060'
    __db_name = 'tripnow'
    __db = ''

    def __init__(self):
        self.__db = self.db_connect()

    def __del__(self):
        self.__db.close()

    def db_connect(self):
        self.__db = pymysql.connect(self.__db_url, self.__db_username,
                                    self.__db_password, self.__db_name)
        return self.__db

    def db_insert(self, sql):
        self.__init__()
        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            self.__db.commit()
            return result[0]
        except:
            self.__del__()