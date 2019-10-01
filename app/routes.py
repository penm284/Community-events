import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

#name of database
app.config['MONGO_DBNAME'] = 'events'

app.config['MONGO_URI'] = 'mongodb+srv://admin:paQYItRoMs9pfF4N@cluster0-lfs7i.mongodb.net/events?retryWrites=true&w=majority'
mongo = PyMongo(app)
#index home page
@app.route('/')
@app.route('/index')

def index():
    #connect to database
    collection = mongo.db.events
    #search database for all events
    events = list(collection.find({}))
    #shows html
    return render_template('index.html', events = events)



@app.route('/input')
def input():
    #shows html
    return render_template('input.html')
#stores data from form
@app.route('/results', methods = ["Get", "Post"])
def results():
    #requests userdata from form and converts to dict
    userdata = dict(request.form)
    print(userdata)
    #storing event variables
    event_name = userdata['event_name']
    event_date = userdata['event_date']
    event_type = userdata['event_type']
    #connecting to mongo
    events = mongo.db.events
    events.insert({'name': event_name, 'date': event_date, 'type': event_type})
    #search database for all events
    events = list(events.find({}))
    print(events)
    #html
    return render_template('index.html', events = events)

@app.route('/delete_events')
def delete_events():
    events = mongo.db.events

    events.delete_many({})
    print ("Documents Deleted")
