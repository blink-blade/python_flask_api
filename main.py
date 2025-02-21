
"""basic Flask app - demo of using a variable in a route"""
import requests
from flask import Flask, jsonify
from db import db_session, User

app = Flask(__name__)

@app.route('/')
def hello():
    with open('main.html', 'r') as file:
        return file.read()

@app.route('/read/<name>')
def user(name):
    user = db_session.query(User).filter_by(name=name).first()
    return user.as_dict()

@app.route('/read_all/')
def read_all():
    users = {}
    user_list = db_session.query(User).all()
    for user in user_list:
        users[user.name] = user.as_dict()
    return users

@app.route('/post/password=<password>_name=<name>_email=<email>')
def create(name, password, email):
    if db_session.query(User).filter_by(name=name).first():
        return 'User already exists.'

    user = User(name=name, email=email, password=password)
    db_session.add(user)
    db_session.commit()
    return 'User Added'

if __name__ == '__main__':
    app.run(debug=True)
