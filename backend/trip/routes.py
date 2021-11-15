from trip.models import *
from trip import app, db
from trip.controllers import DatabaseOperations, User_query
from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import login_user

# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# route for ping.vue
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.json.get('phone')
        password = request.json.get('password')
        res = User_query(phone,password)
        if res is not None:
            test_admin_user = CalendarAdmin(phone)
            login_user(test_admin_user)
            session['uid'] = res.id
            name = res.user_name
            return jsonify({'status':'ok','info':'%s登录成功'%name,'session':name})
        return jsonify({'status':'no','info':'登录失败'})
    return jsonify({'status':'no','info':'登录失败'})


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        phone = request.json.get('phone')
        exist = db.session.query(User).filter(User.phone==phone).first()
        if exist is not None:
            return jsonify({'status':'no','info':'该手机号已被注册！'})
        else:
            password = request.json.get('password')
            email = request.json.get('email')
            user_name = request.json.get('user_name')
            print(user_name)
            user = User(user_name=user_name, email=email, phone=phone,
                    password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'status':'ok','info':'注册成功'})
    return jsonify({'status':'no','info':'注册失败！'})

# @app.route('/plan',methods=['GET', 'POST'])
# def get_attrctions():
#     interest = request.json.get('interest')
#     print(interest)
#     result = []
#     for item in interest:
#          attractions = db.session.query(Attraction).filter(Attraction.attraction_label==item).order_by(Attraction.id)
#          for attraction in attractions:
#              result.append(attraction.basic_to_json())
#     return jsonify(data=result)


@app.route('/users',methods=['GET', 'POST'])
def get_users():
    res = db.session.query(User).all()				#User是从models里导入的 
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(data=temp)


@app.route('/<path:fallback>')
def fallback(fallback):       # Vue Router 的 mode 为 'hash' 时可移除该方法
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')
