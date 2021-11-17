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
        
import requests
import re

# dijkstra算法实现，有向图和路由的源点作为函数的输入，最短路径最为输出
AK = 'nGv0mHXo2BGuNmN4s7nazQSSBnZs4PGQ'

def dijkstra(graph, src):
    # 判断图是否为空，如果为空直接退出
    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # 获取图中的所有节点
    visited = []   # 表示已经路由到最短路径的节点集合
    if src in nodes:  # 如果该节点未被标记
        visited.append(src)  # 标记该节点
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}  # 记录源节点到各个节点的距离
    for i in nodes:
        distance[i] = graph[src][i]  # 初始化
    path = {src: {src: []}}  # 记录源节点到每个节点的路径
    k = pre = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance  # 进行距离更新
                    k = d
                    pre = v
        distance[k] = mid_distance  # 最短路径
        path[src][k] = [i for i in path[src][pre]]
        path[src][k].append(k)
        # 更新两个节点集合
        visited.append(k)
        nodes.remove(k)
    return distance, path

def get_routes(attraction_names, num):
    # 创建字典存储点位信息
    graph_list = []
    # 创建列表存储距离/时间信息

    head = {'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

    num = int(num)
    a = {}
    for i in range(1, num+1):
        m = i
        a[i] = str(attraction_names[i-1])

    for i in range(1, num+1):
        list = []  # 列表存储中间的距离/时间
        for m in range(1, num+1):
            url1 = "http://restapi.amap.com/v3/place/text?key=a5bdc752b8e54575e6bd2b9d5aad7575&keywords=%s&types=&city=珠海&output=json" % (a[i])
            data1 = requests.get(url1, headers=head)
            data1.encoding = 'utf-8'
            data1 = data1.text
            pat1 = 'location":"(.*?),(.*?)",".*?ddress'
            result1 = re.findall(pat1, data1)
            

            url2 = "http://restapi.amap.com/v3/place/text?key=a5bdc752b8e54575e6bd2b9d5aad7575&keywords=" + a[m]\
                + "&types=&city=珠海&children=1&offset=1&page=1&extensions=all"
            data2 = requests.get(url2, headers=head)
            data2.encoding = 'utf-8'
            data2 = data2.text
            result2 = re.findall(pat1, data2)
            print(result2)

            url3 = "http://restapi.amap.com/v3/distance?key=a5bdc752b8e54575e6bd2b9d5aad7575&origins=" +\
                str(result1[0][0]) + "," + str(result1[0][1]) + "&destination=" + str(result2[0][0]) + "," +\
                str(result2[0][1])+"&type=1"
            data3 = requests.get(url3, headers=head)
            data3.encoding = 'utf-8'
            data3 = data3.text
            pat2 = "distance\":\"(.*?)\",\"duration\":\"(.*?)\""
            result3 = re.findall(pat2, data3)
            # 获得两个节点的距离/时间信息
            list.append(int(result3[0][0]))

        graph_list.append(list)
        # 将所有的距离/时间信息存储到列表中

    distance, path = dijkstra(graph_list, 0)  # 查找从源点0开始带其他节点的最短路径 

    time = 0
    result = []
    for key in path[0]:
        result.append(a[key+1])
    return result