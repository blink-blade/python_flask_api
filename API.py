
import requests
from flask import Flask, jsonify, request, render_template

from base import app
from db import db_session, User



@app.route('/')
def hello():
    return render_template('main.html', example=[1, 2, 3])

@app.route('/user/read/<id>')
def user(id):
    user = db_session.query(User).filter_by(id=id).first()

    if not user:
        return {'error': f'Could not find user by id {id}.'}, 400
    print(user.as_dict())
    return user.as_dict()

@app.route('/read_all/')
def read_all():
    users = {}
    user_list = db_session.query(User).all()

    for user in user_list:
        users[user.name] = user.as_dict()
        print(user.as_dict())

    if not users:
        return {'error': 'No users.'}, 400

    return users

@app.route('/user/add', methods=['POST'])
def create():
    print('hay')
    print(request.json)
    if not request.is_json:
        print('not valid json')
        return {'error': 'Is not valid json.'}, 400

    for string in ['name', 'password', 'email']:
        if not request.json.get(string):
            return {'error': f'Missing parameter: {string}'}, 400

    user = db_session.query(User).filter_by(id=request.json.get('id')).first()
    # print(user.__table__.columns)
    if user:
        print('User already exists')
        return {'error': f'User {user.name} already exists.'}, 400

    user = User(name=request.json.get('name'), email=request.json.get('email'), password=request.json.get('password'))
    db_session.add(user)
    db_session.commit()
    print(user.as_dict())
    return user.as_dict()

@app.route('/user/modify', methods=['PUT'])
def modify():
    if not request.is_json:
        return {'error': 'Is not valid json.'}, 400

    if not request.json.get('id'):
        return {'error': f'Missing parameter: id'}, 400

    user = db_session.query(User).filter_by(id=request.json.get('id')).first()

    if not user:
        return {'error': f'Could not find user by id {request.json.get("id")}.'}, 400

    for key in request.json.keys():
        if key == 'id':
            continue
        setattr(user, key, request.json.get(key))

    db_session.commit()
    return user.as_dict()
