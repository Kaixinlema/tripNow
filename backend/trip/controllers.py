from trip.models import *
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange, Optional
from flask_login import UserMixin
from trip import db
import pymysql
import requests
import re

# function to inquire the user information
def User_query(phone,password):
    res = db.session.query(User).filter(User.phone==phone).filter(User.password==password).first()
    if res is not None:
        return res

# key for using the map api
AK = 'nGv0mHXo2BGuNmN4s7nazQSSBnZs4PGQ'

def dijkstra(graph, src):
    # check whether the input is empty
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # get all the nodes in the graph
    visited = []  
    if src in nodes:  # if the node is not marked
        visited.append(src)  # mark the node
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}  # record the distance
    for i in nodes:
        distance[i] = graph[src][i]  # Initialization
    path = {src: {src: []}}  # record the route
    k = pre = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance  # update the distance
                    k = d
                    pre = v
        distance[k] = mid_distance  # the shortest route
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)
        # update the set
        visited.append(k)
        nodes.remove(k)
    return distance, path

def get_routes(attraction_names, num):
    graph_list = []
  
    head = {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

    num = int(num)
    a = []
    for i in range(0, num):
        a.append(str(attraction_names[i-1]))
    
    # get the longtitude and the latitude of the attractions
    location = [[0 for i in range(2)] for i in range(num)]
    for k in range(0,num):
        url = "http://restapi.amap.com/v3/place/text?key=a5bdc752b8e54575e6bd2b9d5aad7575&keywords=%s&types=&city=珠海&output=json" % (a[k])
        data = requests.get(url, headers=head)
        data.encoding = 'utf-8'
        data = data.text
        pat = 'location":"(.*?),(.*?)",".*?ddress'
        result = re.findall(pat, data)
        location[k][0] = result[0][0]
        location[k][1] = result[0][1]

    for i in range(0, num):
        list = []  
        for m in range(0, num):
            url3 = "http://restapi.amap.com/v3/distance?key=a5bdc752b8e54575e6bd2b9d5aad7575&origins=" +\
                str(location[i][0]) + "," + str(location[i][1]) + "&destination=" + str(location[m][0]) + "," +\
                str(location[m][1])+"&type=1"
            data3 = requests.get(url3, headers=head)
            data3.encoding = 'utf-8'
            data3 = data3.text
            pat2 = "distance\":\"(.*?)\",\"duration\":\"(.*?)\""
            result3 = re.findall(pat2, data3)
            # get the information of distance between two nodes
            list.append(int(result3[0][0]))

        graph_list.append(list)
        # store all the information

    distance, path = dijkstra(graph_list, 0)  # find the shortest route

    result = []
    for key in path[0]:
        if a[key] not in result:
            result.append(a[key])
    return result