# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 30-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from flask import Flask
import json


app = Flask(__name__)

buses = json.load(open('buses.json'))

@app.route("/distance")
def distance_handler():
    return 10


@app.route('/buses')
def busese_hadler():
    result = []
    for b in buses:
        result.append(b['id'])
    return json.dumps(result)


@app.route("/buses/<int:bus_id>")
def buses_handler(bus_id):
    result = {}
    for b in buses:
        if b['id'] == bus_id:
            result = b
    return json.dumps(result)


if __name__ == "__main__":
    app.run("0.0.0.0", 1373)
