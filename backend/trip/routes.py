# file to store all routes

from trip.models import *
from trip.controllers import get_routes
from trip import app, db
from trip.controllers import User_query
from flask import jsonify, request, session
import re

# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# route for login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get the information from the frontend
        phone = request.json.get('phone')
        password = request.json.get('password')
        # query the database to find if the user exists
        res = User_query(phone,password)
        # if the user exists
        if res is not None:
            session['uid'] = res.id
            name = res.user_name
            return jsonify({'status':'ok','info':'%s登录成功'%name,'session':name})
        return jsonify({'status':'no','info':'登录失败'})
    return jsonify({'status':'no','info':'登录失败'})

# route for register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # get the information from the frontend
        phone = request.json.get('phone')
        # query the database to make sure the phone number had not been registered
        exist = db.session.query(User).filter(User.phone==phone).first()
        # if the phone has been registered
        if exist is not None:
            return jsonify({'status':'no','info':'该手机号已被注册！'})
        # if not, create a new user and insert the data into database
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

# route for make the plan, to recommend the route, other attractions and hotels to user
@app.route('/choice',methods=['GET', 'POST'])
def get_route():
    # get information from the frontend
    raw_interest = request.json.get('choices')
    type = request.json.get('type')  
    number = request.json.get('number')
    attraction_names = []
    price = 0

    print(number)

    interest = [] # list to store the selected attractions' id
    for i in raw_interest:
        if isinstance(i, int):
            interest.append(i)
        else: 
            interest.append(i["id"])
    
    # get the name of the selected attractions
    for item in interest:
        tmp = db.session.query(Attraction).filter(Attraction.id==item).first()
        name = tmp.to_json()['attraction_name']
        price += tmp.to_json()['attraction_cost']
        attraction_names.append(name)

    # get the recommended attractions
    consequent_result = []
    for item in interest:
        # query the association rule database
        rules = db.session.query(Rule).filter(Rule.antecents.contains(str(item))).first()
        if (rules):
            consequent_id = rules.to_json()['consequents']
            consequent_id_todigit = (re.findall('\d+', consequent_id))
            for item in consequent_id_todigit:
                # if the found attraction has neither been selected nor recommended
                if (int(item) not in interest) and (int(item) not in consequent_result):
                    consequent_result.append(int(item))

    # get the shortest route
    route = get_routes(attraction_names, len(attraction_names))
    route_result = []
    for poi in route:
        info = db.session.query(Attraction).filter(Attraction.attraction_name==str(poi)).first().to_json()
        if (info["id"]) not in route_result:
            route_result.append(info)

    # plan every day's route
    day = []  # list to store the daily attraction
    time = 0  # to calculate the accumulated time
    num = 1   # to calculate the total days
    for i in range (0, len(route_result)):
        # add the first attraction to the list
        if i == 0:
            day.append({
                'day': num,
                'attraction': route_result[i]})
            time += route_result[i]["attraction_time"]
        # for middle attractions
        elif i!=len(route_result)-1:
            # if the time for this attraction is more than 6 hours, then we suppose the user will spend the whole day on it
            if route_result[i]["attraction_time"] > 6:
                num+=1
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                    })
                time=0
            # if the accumulated time for this day does not exceed 6 hours, arrange this attraction to this day
            elif time+route_result[i]["attraction_time"] <= 6:
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time+=route_result[i]["attraction_time"]
            # if the accumulated time for this day exceeds 6 hours, arrange this attraction to next day
            elif time+route_result[i]["attraction_time"] > 6:
                num+=1
                time=0
                day.append({
                    'day': num,
                    'attraction': route_result[i]})
                time+=route_result[i]["attraction_time"]
        # for the last attraction
        elif i==len(route_result)-1:
            # if the expected time cost for this attraction exceeds 6 hours, arrange one more day for it
            if route_result[i]["attraction_time"] > 6:
                num+=1
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time = 0
            # otherwise, arrange this attraction to the last day
            elif route_result[i]["attraction_time"] <= 6:
                day.append({
                    'day': num,
                    'attraction': route_result[i]
                })
                time=0

    # get the recommended hotel
    hotel = []
    for k in range(0,len(day)):
        # recommend the hotels whick are near to the last visited attraction for each day
        if k == len(day)-1 or day[k]['day'] != day[k+1]['day']:
            res = db.session.query(Hotel).filter(Hotel.attraction_id==day[k]["attraction"]['id']).filter(Hotel.type==type).first().to_json()
            hotel.append(res)
            price += res["price"]
    # estimate the total cost
    price += num * 100 + len(day)*30/int(number)

    return jsonify({'recommend': consequent_result,
                    'route': route_result,
                    'day': day,
                    'numofday': num,
                    'hotel': hotel,
                    'cost': price})

# route for other apis
@app.route('/<path:fallback>')
def fallback(fallback):      
    if fallback.startswith('css/') or fallback.startswith('js/')\
            or fallback.startswith('img/') or fallback == 'favicon.ico':
        return app.send_static_file(fallback)
    else:
        return app.send_static_file('index.html')
