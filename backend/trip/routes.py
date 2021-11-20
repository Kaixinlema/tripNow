from trip.models import *
from trip.controllers import get_routes, dijkstra
from trip import app, db
from trip.controllers import DatabaseOperations, User_query
from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import login_user
import json, re

# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# route for ping.vue
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# route for login 
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

# route for register
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

# route for make the plan
@app.route('/choice',methods=['GET', 'POST'])
def get_route():
    interest = request.json.get('choices')
    type = request.json.get('type')
    print(type)
    attraction_names = []
    price = 0

    # get the name of the selected attractions
    for item in interest:
        if isinstance(item, int):
            tmp = db.session.query(Attraction).filter(Attraction.id==item).first()
        else:
            tmp = db.session.query(Attraction).filter(Attraction.id==item["id"]).first()
        name = tmp.to_json()['attraction_name']
        price += tmp.to_json()['attraction_cost']
        attraction_names.append(name)

    # get the recommended attractions
    consequent_result = []
    for item in interest:
        if isinstance(item, int):
            rules = db.session.query(Rule).filter(Rule.antecents.contains(str(item))).first()
        else:
            rules = db.session.query(Rule).filter(Rule.antecents.contains(str(item["id"]))).first()
        if (rules):
            consequent_id = rules.to_json()['consequents']
            consequent_id_todigit = (re.findall('\d+', consequent_id))
            for item in consequent_id_todigit:
                if (int(item) not in interest) and (int(item) not in consequent_result):
                    # attraction = db.session.query(Attraction).filter(Attraction.id==int(item)).first().to_json()
                    consequent_result.append(int(item))

    # get the shortest route
    route = get_routes(attraction_names, len(attraction_names))
    route_result = []
    for poi in route:
        info = db.session.query(Attraction).filter(Attraction.attraction_name==str(poi)).first().to_json()
        if (info["id"]) not in route_result:
            route_result.append(info)

    # plan every day's route
    day = []
    time = 0
    num = 1
    for i in range (0, len(route_result)):
        if i == 0:
            day.append({
                'day': num,
                'attraction': route_result[i]})
            time += route_result[i]["attraction_time"]
        if time >= 6:
            num+=1
            time = 0
        elif i!=len(route_result)-1 and i!=0:
            if route_result[i]["attraction_time"] >6:
                num+=1
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                    })
                num+=1
                time=0
            elif time+route_result[i]["attraction_time"]<=6:
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time+=route_result[i]["attraction_time"]
            elif time+route_result[i]["attraction_time"]>6:
                num+=1
                time=0
                day.append({
                    'day': num,
                    'attraction': route_result[i]})
                time+=route_result[i]["attraction_time"]
        elif i==len(route_result)-1:
            if route_result[i]["attraction_time"] > 6:
                num+=1
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time = 0
            elif route_result[i]["attraction_time"] <= 6:
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time=0
    print(day)


    # get the recommended hotel
    hotel = []
    for k in range(0,len(day)):
        if k == len(day)-1 or day[k]['day'] != day[k+1]['day']:
            res = db.session.query(Hotel).filter(Hotel.attraction_id==day[k]["attraction"]['id']).filter(Hotel.type==type).first().to_json()
            hotel.append(res)
            price += res["price"]
    print(hotel)


    return jsonify({'recommend': consequent_result,
                    'route': route_result,
                    'day': day,
                    'numofday': num,
                    'hotel': hotel,
                    'cost': price})


@app.route('/users',methods=['GET', 'POST'])
def get_users():
    res = db.session.query(User).all()		
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
