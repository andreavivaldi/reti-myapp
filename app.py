import os
from flask import Flask
from flask import render_template
import socket
import random
import os
import json
from flask_pymongo import PyMongo

app = Flask(__name__)

dbUri = os.environ.get('DB_URI') or 'mydb'
dbUser = os.environ.get('DB_USER') or 'myapp'
dbPassword = os.environ.get('DB_PASSWORD') or 'mypwd'
dbDatabase = os.environ.get('DB_DATABASE') or 'colors'

envuse = False
dbuse = False
colorCodeHash = "#000000"

if os.environ.get('DB_URI') and os.environ.get('DB_USER') and os.environ.get('DB_PASSWORD') and os.environ.get('DB_DATABASE'):
    envuse = True

try:
    app.config["MONGO_URI"] = "mongodb://" + dbUser + ":" + dbPassword + "@" + dbUri + ":27017/" + dbDatabase
    mongo = PyMongo(app)
    colorName = random.choice(["red","green","blue","blue2","darkblue","pink"])
    colorCode = mongo.db.colors.find_one( { 'name': colorName }, { 'color': 1, '_id': 0} )
    colorCodeHash = colorCode['color']
    dbuse = True
except Exception as e:
    print(e)

@app.route("/")
def main():
    return render_template('hello.html', envuse=envuse, name=socket.gethostname(), dbuse=dbuse, color=colorCodeHash)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
