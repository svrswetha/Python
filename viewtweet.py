#!/usr/local/bin/python3.4
import sys
import proxy
from flask import Flask
from pymongo import MongoClient
from flask import render_template
#from flask import request
#from bson import json_util

app = Flask(__name__)
_MONGO_HOST_ = 'localhost'
_MONGO_PORT_ = 27017

@app.route('/testDb', methods=['GET'])
def test():
    '''
    Function to demo connecting to database and submitting query.
    Assumptions:
        MongoDB Host = _MONGO_HOST_
        MongoDB Port = _MONGO_PORT_
        MongoDB Has database: 'test_db'
        MongoDB Has collection in that database: 'test'
        db_test.test has documents of the form:
            item['_id'] - object unique id
            item['text'] - Some text
            item['value'] - Integer value
        At least 1 item with item['value'] < 3 and 1 item with item['value'] > 3
    '''
    client = MongoClient(_MONGO_HOST_, _MONGO_PORT_)
    db = client.test_db
    collection = db.test
    smaller_than_three = [item for item in collection.find({"value":{"$lt":3}}).limit(1)][0]
    greater_than_three = [item for item in collection.find({"value":{"$gt":3}}).limit(1)][0]
    return render_template("testDb.html", smaller=smaller_than_three, larger=greater_than_three)

@app.route('/', methods=['GET'])
def index():
    '''
    Function to show landing page.
    '''
    return render_template("landing.html")

@app.route('/tweet', methods=['GET'])
def viewTweet():
    '''
    Function to view single tweets.
    '''
    return "<html><body><h1 style='text-align:center;width:100%;'>Not ready yet</h1></body></html>"

if __name__ == "__main__":
    args = sys.argv
    server_parameters = {'host': '0.0.0.0',
                         'threaded': True,
                         'debug': True,
                         'port': int(args[1]) if len(args) > 1 else 6666}
    proxy_script_name = args[2] if len(args) > 2 else '/claimportal'
    #app.wsgi_app = proxy.ReverseProxied(app.wsgi_app, script_name=proxy_script_name)
    app.run(**server_parameters)
