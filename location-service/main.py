# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 30-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from flask import Flask
app = Flask(__name__)


@app.route("/distance")
def distance_handler():
    return 10


@app.route("/buses")
def buses_handler():
    times = [10, 20]
    result = ""
    for time in times:
        result = result + " " + str(time)
    return result


if __name__ == "__main__":
    app.run("0.0.0.0", 1373)
