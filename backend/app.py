from flask import Flask, jsonify, request
from flask_cors import CORS
 
DEBUG = True


app = Flask(__name__)
# app = Flask(__name__)
app = Flask(
    __name__, static_folder="..frontend/dist/static", template_folder="..frontend/dist")

# 解决跨域问题 
# CORS(app, resources={r'/*': {'origins': '*'}})
 
@app.route('/')
def index():
    return app.send_static_file('index.html')
 
@app.route('/accounts', methods=['GET'])
def get_accounts():
    if request.method == "GET":
        username = request.args.get("account")
        name = "aaa" #query_account(username)
        if name == "":
            return "no result"
        else:
            #return render_template("home.html",message=username,password=password)
            return jsonify({"name": name})


 
 
if __name__ == '__main__':
    app.run()