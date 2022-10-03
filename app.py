import pymysql
import time
from flask import Flask

time.sleep(5)
app = Flask(__name__)


@app.route("/select", methods=["GET"])
def select():
    juso_db = pymysql.connect(
        user='flask01',
        password='flask01',
        host='mariadb01',
        port=3000,
        db='flask01_db',
        charset='utf8'
    )
    cursor = juso_db.cursor()
    sql = "select id, email, phone_number from private;"
    cursor.execute(sql)
    row = cursor.fetchall()
    print(row)

    lst = []
    for data in row:
        dic = {
            'id' : data[0],
            'email' : data[1],
            'phone_number' : data[2]
        }
        lst.append(dic)

    juso_db.close()

    return str(lst)


@app.route('/')
def hello_world():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)