from trip.models import *
from trip import app, db
from flask import Flask, jsonify, request, render_template, make_response


# route for home page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# route for ping.vue
@app.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

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
