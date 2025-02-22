
"""basic Flask app - demo of using a variable in a route"""
import requests
from flask import Flask, jsonify, request
from db import db_session, User

app = Flask(__name__)

@app.route('/')
def hello():
    with open('main.html', 'r') as file:
        return file.read()

@app.route('/read/<name>')
def user(name):
    return user.as_dict()

@app.route('/read_all/')
def read_all():
    users = {}
    user_list = db_session.query(User).all()
    for user in user_list:
        users[user.name] = user.as_dict()
    return users

@app.route('/user/add', methods=['POST'])
def create():
    if not request.is_json:
        return {'error': 'Is not valid json.'}, 400

    for string in ['name', 'password', 'email']:
        if not request.json.get(string):
            return {'error': f'Missing parameter: {string}'}, 400


    user = db_session.query(User).filter_by(name=request.json.get('name')).first()
    if user:
        return {'error': f'User {user.name} already exists.'}, 400

    user = User(name=request.json.get('name'), email=request.json.get('email'), password=request.json.get('password'))
    db_session.add(user)
    db_session.commit()
    return user.as_dict()

if __name__ == '__main__':
    app.run(debug=True)
