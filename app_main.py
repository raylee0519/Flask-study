import pymysql
import time
import requests
from flask import Flask
import json

time.sleep(5)

app = Flask(__name__)

@app.route('/result', methods=["GET"])
def hello():

    res1 = requests.get('http://flask01:8000/select')
#    res2 = requests.get('http://flask02:8000')

#    //res1, res2의 결과를 가공
#    //...

    return str(res1.text)


@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)