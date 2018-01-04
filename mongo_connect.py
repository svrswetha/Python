from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId


# app = Flask(__name__)
# app.config['MONGO_DBNAME'] = 'connecttomongo'
# app.config['MONGO_URL'] = 'mongodb://svrswetha:RagSwe@5992@ds227555.mlab.com:27555/connecttomongo'
#
# mongo = PyMongo(app)
#
# @app.route('/add')
# def add():
#   user = mongo.db.users
#   user.insert({'name':'Swetha'})
#   return 'Added User'
#
# if __name__ == '__main__':
#   app.run(debug=True)

# app = Flask(__name__)
# app.config['MONGO_DBNAME'] = 'connecttomongo'
# app.config['MONGO_URL'] = 'http://idir-server2.uta.edu:80/factchecker/score_text/'
# MONGO_HOST = 'mongodb://localhost/twitter_db'
# client = MongoClient(MONGO_HOST)
# db = client.twitter_db
#   #'mongodb://svrswetha:RagSwe@5992@ds227555.mlab.com:27555/connecttomongo'
# mongo = PyMongo(app)
# @app.route('/single_tweet')
# def single_tweet():
#   test_dba = mongo.db.test
#   return 'Connected'
#
#   #user.insert({'text': "testing, testing 123", 'value': 4})
#   #user.insert({'text': "testing, testing 321", 'value': 2})
# #  return hi
#
# if __name__ == '__main__':
#   app.run(debug=True)

# from flask import Flask, request
# app = Flask(__name__)
#
# @app.route('/')
# def main_form():
#     return '<form action="submit" id="textform" method="post"><textarea name="text">Hello World!</textarea><input type="submit" value="Submit"></form>'
#
# @app.route('/submit', methods=['POST'])
# def submit_textarea():
#     return "You entered: {}".format(request.form["text"])
#
# if __name__ == '__main__':
#     app.run()


# Create a new connection to a single MongoDB instance at host:port.
connection = MongoClient()

# Create and get a data base (db) from this connection
db = connection.test

# Create and get a collection named "collect" from the data base named "db" from the connection named "connection"
collection = db.collect

# Create an entry and insert in the collection
age = 30
entry = {"Name": "Ralph",
         "Address": "16, Av Foch",
         "Age in Years": age}
collection.insert(entry)


# Print out the inserted entry
print(list(collection.find()))

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'connecttomongo'
app.config['MONGO_URL'] = 'http://idir-server2.uta.edu:80/factchecker/score_text/'
MONGO_HOST = 'mongodb://localhost/twitter_db'
client = MongoClient(MONGO_HOST)
db = client.twitter_db
mongo = PyMongo(app)

@app.route('/single_tweet')
def single_tweet():
  test_dba = mongo.db.test
  return t3
# close connection
connection.close()

if __name__ == '__main__':
  app.run(debug=True)
